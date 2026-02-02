
---

# Airflow DAG 작성 및 데이터 공유

이 문서는 Airflow의 오퍼레이터(Operator) 활용, DAG 실행 흐름 제어, 스케줄링 개념, 그리고 Task 간 데이터 공유(XCom, Variable)에 대한 내용을 다룹니다.

## 1. 오퍼레이터 (Operator) 기본

오퍼레이터는 DAG 내에서 수행될 실제 작업(Task)을 정의하는 템플릿입니다.

### 1.1 Action Operators

실제 작업을 수행하거나 외부 시스템과 상호작용하는 오퍼레이터입니다.

* **BashOperator:** 쉘 스크립트(Shell Script)를 실행
* **PythonOperator:** Python 함수를 실행
* **EmailOperator:** 이메일 전송

#### **[코드 예시] BashOperator로 쉘 스크립트 수행**

외부의 `select_fruit.sh` 파일을 실행하거나 인라인 명령어를 실행합니다.

**쉘 스크립트 (`select_fruit.sh`) 내용:**

```bash
#!/bin/bash
FRUIT=$1
if [ $FRUIT == APPLE ]; then
    echo "You selected Apple!"
elif [ $FRUIT == ORANGE ]; then
    echo "You selected Orange!"
elif [ $FRUIT == GRAPE ]; then
    echo "You selected Grape!"
else
    echo "You selected other Fruit!"
fi

```

#### **[코드 예시] PythonOperator 사용**

Python 함수를 정의하고 오퍼레이터에서 호출합니다.

```python
# 함수 정의
def my_function():
    print("Hello, Airflow!")

# Task 정의
python_t1 = PythonOperator(
    task_id='python_t1',
    python_callable=my_function
)

```

### 1.2 기타 오퍼레이터

* **EmptyOperator:** Task 실행 없이 DAG의 논리적 흐름(시작, 끝, 그룹화)을 잡을 때 사용합니다.
* **BranchOperator:**
* `BranchPythonOperator`: Python 함수의 결과에 따라 다음에 실행할 Task를 결정합니다.
* API 응답값 등을 기반으로 분기 처리를 할 때 유용합니다.



### 1.3 Airflow Decorators (TaskFlow API)

Python 함수에 데코레이터를 붙여 간결하게 Task를 생성하는 방식입니다.

**주요 구성:**

* `@task`: 파이썬 함수를 Airflow Task로 변환
* 데이터 전달: 함수 간 인자 전달이 자동으로 XCom을 사용하게 됨
* 의존성 설정: 함수 호출 순서대로 의존성이 자동 설정됨

#### **[코드 예시] Airflow Decorators 코드 비교**

```python
from airflow.decorators import task
import pendulum

# @task 데코레이터로 함수를 Task로 변환
@task
def extract_data():
    print("Extracting data...")
    return "raw_data"

@task
def transform_data(data):
    print(f"Transforming {data}...")
    return "transformed_data"

@task
def load_data(data):
    print(f"Loading {data}...")
    return "Loaded!"

# DAG 컨텍스트 내에서 호출 (실제 DAG 정의 부분은 생략됨)
# data = extract_data()
# transformed = transform_data(data)
# load_data(transformed)

```

---

## 2. DAG 실행 흐름 (Scheduling & Trigger)

### 2.1 Task 연결 원리

DAG 내에서 Task 간의 의존성(Dependency)을 설정하여 실행 순서를 결정합니다.

* **Upstream (상위):** 현재 Task 이전에 실행되는 Task
* **Downstream (하위):** 현재 Task 이후에 실행되는 Task
* **연결 방식:** 순차 실행(Sequential)과 병렬 실행(Parallel)

#### **[코드 예시] 다중 Task 연결 (병렬 실행)**

```python
# DAG 연결 설정 (start -> 병렬 실행 -> end)
# start >> [task_1, task_2] >> end

# 상세 흐름 예시
start >> [task_1, task_2]  # start 이후 task_1, task_2 병렬 실행
task_1 >> [task_21, task_3] # task_1 완료 후 task_21, task_3 실행
task_3 >> [task_4, task_5] # task_3 완료 후 task_4, task_5 병렬 실행
# ... (이후 흐름 생략)

```

### 2.2 Trigger Rule (트리거 규칙)

Upstream Task의 성공/실패 여부에 따라 Downstream Task의 실행 여부를 결정하는 규칙입니다.

| Trigger Rule | 설명 |
| --- | --- |
| `all_success` | (기본값) 모든 Upstream Task가 성공(Success) 시 실행 |
| `all_failed` | 모든 Upstream Task가 실패(Fail) 시 실행 |
| `all_done` | 모든 Upstream Task의 실행이 완료(성공/실패 무관)되면 실행 |
| `one_failed` | 최소 1개의 Upstream Task가 실패하면 실행 |
| `one_success` | 최소 1개의 Upstream Task가 성공하면 실행 |
| `none_failed` | Upstream Task 중 실패가 없는 경우 실행 (성공 또는 스킵) |
| `none_skipped` | Upstream Task가 스킵되지 않았으면 실행 |

---

## 3. DAG 및 Task 시간 개념

### 3.1 Logical Date (논리적 날짜)

* DAG run을 식별하는 논리적인 날짜입니다.
* **주의:** 실제 실행 시간(Run at)과 다릅니다. 데이터 관점에서의 처리 기준일입니다.
* 예: `logical_date` = 2025-03-01, `schedule_interval` = @daily인 경우
* **실제 실행:** 2025-03-02 00:00:00 (하루가 다 지난 후 실행)
* 데이터 무결성(Data Integrity)을 위해 해당 기간의 데이터가 모두 쌓인 후 실행한다는 개념입니다.



### 3.2 Schedule Interval 설정

* **Cron 표현식:** 정교한 주기 설정 가능 (예: `0 12 * * *` 매일 12시)
* **Preset:** `@daily`, `@hourly`, `@once` 등
* **Timedelta:** 빈도 기반 실행

#### **[코드 예시] 빈도 설정 (Timedelta)**

```python
dag = DAG(
    dag_id="run_every_3_days_timedelta",
    start_date=datetime(2025, 3, 1),
    schedule_interval=timedelta(days=3), # 정확히 3일 간격으로 실행
    catchup=False
)

```

### 3.3 Backfill (백필)

과거 특정 기간에 대해 DAG를 수동으로 실행하여 데이터를 복구하거나 채우는 작업입니다.

* 명령어 예시: `airflow dags backfill -s 2025-08-11 -e 2025-08-14 example_dag`

---

## 4. XCom을 활용한 데이터 전달

### 4.1 XCom (Cross-Communication)이란?

Airflow Task는 독립적으로 실행되므로 메모리를 공유하지 않습니다. Task 간 작은 크기의 데이터(메타데이터, 파일 경로 등)를 주고받기 위해 XCom을 사용합니다. 대용량 데이터(DataFrame 등) 공유에는 적합하지 않습니다.

### 4.2 사용 방법

1. **PythonOperator Return:** 함수가 값을 반환하면 자동으로 XCom에 `return_value`라는 키로 저장됩니다.
2. **xcom_push / xcom_pull:** 명시적으로 데이터를 밀어넣거나 가져옵니다.

#### **[코드 예시] PythonOperator & BashOperator with XCom**

```python
# 1. 데이터를 보내는 Task (Python)
def push_function(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key='message', value='Hello from push_task')

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_function,
    provide_context=True # Airflow < 2.0 인 경우 필요
)

# 2. 데이터를 받는 Task (Bash)
# jinja 템플릿을 사용하여 xcom 값을 가져옴
pull_task = BashOperator(
    task_id='pull_task',
    bash_command='echo "{{ ti.xcom_pull(task_ids="push_task", key="message") }}"'
)

push_task >> pull_task

```

* **@task 데코레이터 사용 시:** 리턴값이 자동으로 XCom에 저장되므로 별도의 push 과정 없이 변수처럼 할당하여 다음 함수에 넘겨주면 됩니다.

---

## 5. 전역 공유 변수 (Variable)

DAG 간 혹은 전체 Airflow 환경에서 공유해야 하는 설정값(config, secret 등)을 저장합니다.

### 5.1 등록 방법

* **Webserver UI:** Admin -> Variables 메뉴에서 Key, Value 입력 후 Save.

### 5.2 사용 방법 (Python Code)

#### **[코드 예시] Variable 가져오기**

```python
from airflow.models import Variable

# Variable 가져오기
def print_variable_task():
    # 'my_var'라는 키의 값을 가져옴, 없으면 'default_val' 사용
    var_value = Variable.get("my_var", default_var="default_val")
    print(f"Variable Value: {var_value}")

print_var_task = PythonOperator(
    task_id='print_var_task',
    python_callable=print_variable_task
)

```

---

