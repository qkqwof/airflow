# from __future__ import annotations

import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # dag 이름 / 직관적으로 볼 수 있게 파이썬 파일명과 일치 시키는 것이 좋음
    schedule="0 0 * * *", # 크론 스케줄
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"), # dags이 언제부터 돌 것인지
    catchup=False, # 기간 설정 시에 누락된 구간을 돌리지 않음 (False인 경우)
    # dagrun_timeout=datetime.timedelta(minutes=60), # 일정 시간 이상 돌면 timeout
    # tags=["example", "example2"],
    params={"example_key": "example_value"}, # task들에 공통적으로 남겨줄 파라미터 있으면 적어줌
) as dag:

    # [START howto_operator_bash]
    bash_t1 = BashOperator( # task 객체명
        task_id="bash_t1", # task도 객체명과 동일하게 주는 게 안 헷갈림
        bash_command="echo whoami", # 어떤 쉘 스크립트 처리할 것인지
    )
    # [END howto_operator_bash]

    # [START howto_operator_bash]
    bash_t2 = BashOperator( # task 객체명
        task_id="bash_t2", # task도 객체명과 동일하게 주는 게 안 헷갈림
        bash_command="echo $HOSTNAME", # 어떤 쉘 스크립트 처리할 것인지
    )
    # [END howto_operator_bash]

    bash_t1 >> bash_t2 # 테스크들의 순서 정해주기

#     for i in range(3):
#         task = BashOperator(
#             task_id=f"runme_{i}",
#             bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
#         )
#         task >> run_this
# 
#     # [START howto_operator_bash_template]
#     also_run_this = BashOperator(
#         task_id="also_run_this",
#         bash_command='echo "ti_key={{ task_instance_key_str }}"',
#     )
#     # [END howto_operator_bash_template]
#     also_run_this >> run_this_last

# [START howto_operator_bash_skip]
# [docs]this_will_skip = BashOperator(
#     task_id="this_will_skip",
#     bash_command='echo "hello world"; exit 99;',
#     dag=dag,
# )
# # [END howto_operator_bash_skip]
# this_will_skip >> run_this_last
# 
# if __name__ == "__main__":
#     dag.test()