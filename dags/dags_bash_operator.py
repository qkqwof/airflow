from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # dag 이름들 (파이썬 파일명과는 상관 없음, but 일치 시키는 것이 좋음)
    schedule="0 0 * * *", # 크론 스케줄러
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 누락된 부분을 다 돌림(true 일 때...)
    # dagrun_timeout=datetime.timedelta(minutes=60), # 타임 아웃 값 설정
    # tags=["example", "example2"], # 어떤 값으로 설정할 것인지...(optional)
    # params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2

    # [START howto_operator_bash]
    # run_this = BashOperator(
    #     task_id="run_after_loop",
    #     bash_command="echo https://airflow.apache.org/",
    # )
    # # [END howto_operator_bash]
# 
    # run_this >> run_this_last
# 
    # for i in range(3):
    #     task = BashOperator(
    #         task_id=f"runme_{i}",
    #         bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
    #     )
    #     task >> run_this
# 
    # # [START howto_operator_bash_template]
    # also_run_this = BashOperator(
    #     task_id="also_run_this",
    #     bash_command='echo "ti_key={{ task_instance_key_str }}"',
    # )
    # # [END howto_operator_bash_template]
    # also_run_this >> run_this_last

# [START howto_operator_bash_skip]
# this_will_skip = BashOperator(
#     task_id="this_will_skip",
#     bash_command='echo "hello world"; exit 99;',
#     dag=dag,
# )
# # [END howto_operator_bash_skip]
# this_will_skip >> run_this_last
# 
# if __name__ == "__main__":
#     dag.test()
