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


<img width="743" height="551" alt="image" src="https://github.com/user-attachments/assets/a2fe10cf-6bb0-4502-bde7-0c4b7c39791c" />


## Resumo do Projeto

---

## O que é o projeto
Pipeline de dados que coleta preços de criptomoedas BTC, ETH, SOL(Depois vou colocar outras...) em tempo quase real, armazena o histórico na nuvem e exibe em um dashboard

---

## Stack escolhida
| Camada | Tecnologia |
|---|---|
| API de dados | CoinGecko (free tier) |
| Linguagem | Python 3.12 |
| Orquestração | Cloud Functions + Cloud Scheduler |
| Data Lake | Google Cloud Storage |
| Data Warehouse | Google BigQuery |
| Dashboard | Looker Studio (próximo passo) |
| Versionamento | GitHub |

---
