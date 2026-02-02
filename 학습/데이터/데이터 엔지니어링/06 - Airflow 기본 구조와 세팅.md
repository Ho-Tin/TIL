
---

# Apache Airflow 기본 구조와 세팅 요약

## 1. Apache Airflow란?

* **정의:** Python 기반의 데이터 파이프라인 자동화 및 스케줄링 도구.
* **핵심 역할:** 배치(Batch) 프로세스를 효율적으로 관리하는 **워크플로우 오케스트레이션(Workflow Orchestration)** 도구.
* **특징:**
* **Python 기반:** 개발자가 쉽게 접근 가능.
* **확장성:** 다양한 시스템(DB, 클라우드 등)과 통합 가능.
* **UI 제공:** 파이프라인의 상태를 시각적으로 확인하고 모니터링 가능.



## 2. 주요 활용 사례

* **ETL / ELT:** 데이터 수집(Extract), 변환(Transform), 적재(Load) 자동화.
* **MLOps:** 머신러닝 모델 학습 -> 평가 -> 배포 과정 자동화.
* **Business Operations:** 기업의 핵심 비즈니스 데이터 애플리케이션 자동화.

## 3. Airflow 설치 및 환경 세팅 (Docker Compose)

Airflow를 로컬 환경에서 가장 쉽게 실행하는 방법은 Docker와 Docker Compose를 사용하는 것입니다.

### 3.1 디렉토리 구조 생성

먼저 로컬에 Airflow 관련 파일들을 저장할 디렉토리를 생성합니다.

```bash
mkdir airflow-docker
cd airflow-docker
mkdir dags logs plugins config

```

### 3.2 docker-compose.yaml 다운로드

Apache Airflow 공식 문서에서 제공하는 `docker-compose.yaml` 파일을 다운로드합니다.

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'

```

### 3.3 사용자 ID 설정 (.env 파일)

Host OS와 컨테이너 간의 권한 문제를 방지하기 위해 사용자 ID(UID)를 환경 변수로 설정합니다.

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env

```

### 3.4 Airflow 초기화 및 실행

데이터베이스 초기화 및 사용자 계정 생성을 수행한 후, 서비스를 실행합니다.

**1. 초기화 (Database Migration 및 계정 생성)**

```bash
docker compose up airflow-init

```

* `exited with code 0`이 나오면 성공적으로 초기화된 것입니다.

**2. 서비스 실행**

```bash
docker compose up

```

* 실행 후 웹 브라우저에서 `http://localhost:8080`으로 접속하여 Airflow UI를 확인할 수 있습니다.
* 기본 계정/비밀번호: `airflow` / `airflow`

## 4. Airflow 주요 컴포넌트

* **Webserver:** 유저 인터페이스(UI)를 제공하며 DAG와 태스크의 상태를 시각화.
* **Scheduler:** 예약된 작업(DAG)을 모니터링하고 실행 시점이 되면 작업을 예약(Schedule)함.
* **Executor:** 스케줄러 내에서 실제로 태스크를 실행하는 주체 (Local, Celery, Kubernetes 등).
* **Worker:** 실제 작업을 수행하는 노드 (분산 환경에서 사용).
* **Metadata Database:** DAG, 태스크 상태, 변수, 연결 정보 등 메타데이터 저장.
* **DAG Directory:** Python으로 작성된 워크플로우 파일들이 저장되는 공간.

## 5. DAG (Directed Acyclic Graph) 개념 및 구조

### 5.1 DAG란?

* **Directed (방향성):** 작업의 실행 순서가 정해져 있음.
* **Acyclic (비순환):** 순환(Loop) 없이 한 방향으로 흐름.
* **Graph:** 노드(Task)와 엣지(Dependency)로 구성됨.

### 5.2 기본 DAG 작성 예시 (Python 코드)

동영상에 나온 예시를 바탕으로 한 기본적인 DAG 구조입니다.

```python
from datetime import datetime, timedelta
from airflow import DAG
# 필요한 Operator 임포트 (예: Bash 명령어를 실행하기 위한 Operator)
from airflow.operators.bash import BashOperator

# 기본 인자 설정 (모든 태스크에 공통 적용)
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG 정의
with DAG(
    dag_id='example_bash_operator',      # DAG의 고유 ID
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',          # 스케줄링 주기 (매일 실행)
    start_date=datetime(2021, 1, 1),     # 시작 날짜
    catchup=False,                       # 과거 데이터 실행 여부
    tags=['example'],
) as dag:

    # 태스크 정의 (t1, t2)
    
    # t1: 단순히 날짜를 출력하는 Bash 명령어 실행
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # t2: 잠시 대기(sleep)하는 Bash 명령어 실행
    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    
    # 템플릿을 사용한 태스크 예시
    templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
    )

    # 태스크 의존성 설정 (실행 순서)
    # t1 실행 후 t2 실행
    t1 >> [t2, t3]

```

## 6. 스케줄링 (Scheduling)

DAG가 실행되는 주기를 설정하는 방식입니다.

* **Cron 표현식:** `0 0 * * *` (매일 자정 실행) 등 구체적인 설정 가능.
* **Preset:**
* `@once`: 한 번만 실행.
* `@hourly`: 매시간 실행.
* `@daily`: 매일 자정 실행.


* **Timedelta:** `timedelta(days=1)` 처럼 마지막 실행 시점으로부터의 간격 설정.

## 7. 로컬 개발 환경 구성 팁 (`docker-compose.yaml`)

로컬에서 작성한 DAG 파일을 컨테이너 내부로 반영하기 위해 **Volume Mapping**을 설정해야 합니다. `docker-compose.yaml` 파일 내 `volumes` 섹션이 이를 담당합니다.

```yaml
volumes:
  - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
  - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
  - ${AIRFLOW_PROJ_DIR:-.}/config:/opt/airflow/config
  - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins

```

* **설명:** 호스트(내 컴퓨터)의 `./dags` 폴더를 컨테이너 내부의 `/opt/airflow/dags` 경로와 동기화합니다. 이렇게 하면 로컬에서 Python 파일을 수정했을 때 Airflow에 바로 반영됩니다.

---
