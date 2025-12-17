from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Allow Airflow to see src/
sys.path.append("/opt/airflow/src")

from arxiv_fetcher import fetch_and_store

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="arxiv_daily_fetch",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    tags=["arxiv", "data-ingestion"],
):
    fetch_task = PythonOperator(
        task_id="fetch_arxiv_papers",
        python_callable=fetch_and_store,
    )

    fetch_task
