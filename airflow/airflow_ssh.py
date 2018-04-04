# -*- coding: utf-8 -*-

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator


"""

    data_source
    etl

"""


default_args = {
    'owner': 'diggzhang',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['diggzhang@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_reporter_airflow',
    default_args=default_args,
    description='offline daily report scripts',
    schedule_interval=timedelta(days=1))

sleep_3_sec = BashOperator(
    task_id='99_sleep_3_sec',
    depends_on_past=False,
    bash_command='sleep 3 && date',
    dag=dag)

online_task01_onions_data_soruce = SSHOperator(
    task_id='online_prepare_onions_data',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh online01',
    timeout=10,
    dag=dag
)

online_task02_orders_data_soruce = SSHOperator(
    task_id='online_prepare_orders_data',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test_sleep_20.sh online02',
    timeout=10,
    dag=dag
)

# task#01 Prepare the underlying data source
# 这部分可以把数仓环节拆出ter去
task_01_prepare_underlying_data_source = SSHOperator(
    task_id='01_prepare_underlying_data',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 01',
    timeout=10,
    dag=dag
)


task_02_users_collection_monitor_data_source = SSHOperator(
    task_id='02_users_collection_monitor',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 02',
    timeout=10,
    dag=dag
)

task_03_tianji_underlying_data_source = SSHOperator(
    task_id='03_tianji_underlying_data_source',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 03',
    timeout=10,
    dag=dag
)

task_04_etl_underlying_data_source = SSHOperator(
    task_id='04_etl_underlying_data_source',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 04',
    timeout=10,
    dag=dag
)

task_05_videology_data_source = SSHOperator(
    task_id='05_videology_data_source',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 05',
    timeout=10,
    dag=dag
)

task_06_marketing_data_reporter = SSHOperator(
    task_id='06_marketing_data_reporter',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 06',
    timeout=10,
    dag=dag
)

task_07_bend_reporter = SSHOperator(
    task_id='07_bend_reporter',
    ssh_conn_id='ssh_default',
    command='/bin/bash /tmp/test.sh 07',
    timeout=10,
    dag=dag
)

online_task01_onions_data_soruce.set_downstream(online_task02_orders_data_soruce)
online_task02_orders_data_soruce.set_downstream(task_01_prepare_underlying_data_source)
task_01_prepare_underlying_data_source.set_downstream(task_02_users_collection_monitor_data_source)
task_02_users_collection_monitor_data_source.set_downstream(task_03_tianji_underlying_data_source)
task_02_users_collection_monitor_data_source.set_downstream(task_04_etl_underlying_data_source)
task_03_tianji_underlying_data_source.set_downstream(task_05_videology_data_source)
task_03_tianji_underlying_data_source.set_downstream(task_06_marketing_data_reporter)
task_03_tianji_underlying_data_source.set_downstream(task_07_bend_reporter)
task_07_bend_reporter.set_downstream(sleep_3_sec)
