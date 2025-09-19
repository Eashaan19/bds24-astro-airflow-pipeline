from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello():
    print("Hello from DAG!")

default_args = {'start_date': datetime(2024,1,1)}

with DAG('example', default_args=default_args, schedule_interval='@daily') as dag:
    task = PythonOperator(task_id='hello_task', python_callable=hello)
