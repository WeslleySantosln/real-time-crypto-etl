**Roteiro do projeto**

Fase 1
Configurar a conta GCP, habilitar BigQuery e Cloud Storage, criar um projeto e instalar as dependências Python localmente.

Fase 2 — Extração
Escrever o script Python que consome a CoinGecko API (/coins/markets), valida os dados e salva em formato Parquet no GCS.

Fase 3 — Airflow + DAG
Configurar o Airflow via Cloud Composer (free trial) ou localmente via Docker. Criar a DAG que agenda a extração a cada 5 minutos.

Fase 4 — BigQuery
Criar as tabelas particionadas por data e escrever a camada de transformação com SQL — preço médio, volatilidade, variação 24h.

Fase 5 — Dashboard
Conectar o Looker Studio ao BigQuery e montar os gráficos: série temporal de preço, variação percentual e volume.


<img width="1440" height="1262" alt="image" src="https://github.com/user-attachments/assets/55b3da30-ceef-470a-a475-4545fbc84ef9" />
