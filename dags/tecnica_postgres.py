from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 3,  # Número de intentos de reintento si falla
    'retry_delay': timedelta(minutes=5),  # Tiempo de espera entre reintentos
}


with DAG(
    dag_id="tecnica_postgres",
    default_args = default_args,
    start_date= datetime(2024,9,20),
    #schedule_interval= '0 0 * * *'
) as dag:
    task_1 = PostgresOperator(
        task_id="Crear_Tabla",
        postgres_conn_id = "postgres_localhost",
        sql = """
            CREATE TABLE IF NOT EXISTS tecnica_ml(
                id VARCHAR(30),
                site_id VARCHAR(30),
                title VARCHAR(50),
                price VARCHAR(10),
                sold_quantity VARCHAR(20),
                thumbnail VARCHAR(50),
                created_date VARCHAR(8),
                primary key(id,created_date)
            )
"""
    )