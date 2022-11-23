from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
	'owner':'aniketh',
	'retries':5,
	'retry_delay':  timedelta(minutes=2 )
}


with DAG(
	dag_id = 'our_first_dag',
	description = 'This is my first airflow dag',
	start_date = datetime(2022, 11,23,2),
	schedule_interval = '@daily'
	) as dag:
  task1 = BashOperator(
	task_id = 'first_task',
        bash_command = "Hello_world, this is my first task"
)

task1
