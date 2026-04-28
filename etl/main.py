import functions_framework
import requests
import pandas as pd
from google.cloud import bigquery, storage
from datetime import datetime, timezone
import json, os

@functions_framework.http
def run_pipeline(request):
    """Ponto de entrada da Cloud Function — chamado pelo Scheduler."""
    try:
        data = extract()
        df   = transform(data)
        load_to_gcs(df)
        load_to_bigquery(df)
        return {"status": "ok", "rows": len(df)}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

def extract():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,solana",
        "order": "market_cap_desc",
        "sparkline": False
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def transform(data):
    rows = []
    for coin in data:
        rows.append({
            "coin_id":        coin["id"],
            "symbol":         coin["symbol"].upper(),
            "price_usd":      coin["current_price"],
            "market_cap":     coin["market_cap"],
            "volume_24h":     coin["total_volume"],
            "change_pct_24h": coin["price_change_percentage_24h"],
            "collected_at":   datetime.now(timezone.utc).isoformat()
        })
    return pd.DataFrame(rows)

def load_to_gcs(df):
    bucket_name = os.environ["GCS_BUCKET"]
    client      = storage.Client()
    bucket      = client.bucket(bucket_name)
    timestamp   = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    blob        = bucket.blob(f"raw/prices_{timestamp}.json")
    blob.upload_from_string(df.to_json(orient="records"), "application/json")

def load_to_bigquery(df):
    project  = os.environ["GCP_PROJECT_ID"]
    dataset  = os.environ["BQ_DATASET"]
    table    = os.environ["BQ_TABLE"]
    client   = bigquery.Client(project=project)
    table_id = f"{project}.{dataset}.{table}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        autodetect=True
    )
    client.load_table_from_dataframe(df, table_id, job_config=job_config).result()