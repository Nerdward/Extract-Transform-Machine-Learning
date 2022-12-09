from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.decorators import task
import boto3

S3_BUCKET = 'mleip-airflow-example-nerdward'
S3_KEY = 'target/target.json'

default_args = {
'owner': 'Ohakim Nnaemeka',
'depends_on_past': False,
'start_date': days_ago(31),
'email': ['eddyhakz@gmail.com'],
'email_on_failure': False,
'email_on_retry': False,
'retries': 1,
'retry_delay': timedelta(minutes=2)
}

 

with DAG(
    'etml pipeline',
    default_args=default_args,
    description='Pipeline for Anomaly Detection',
    schedule_interval=timedelta(days=1), # run daily? check
    ) as dag:

    get_anomalies = BashOperator(
        task_id='get_anomalies',
        bash_command='python3 -m outliers'
        )

    @task
    def upload_to_s3():
        s3 = boto3.client('s3')
        s3.put_object(Bucket=S3_BUCKET, Key=S3_KEY, Body='/usr/local/airflow/scripts/target.json')

    get_anomalies >> upload_to_s3()