
---

# Apache Spark 기본 구조와 세팅

## 1. Spark의 필요성 (Why Spark?)

### 데이터 처리의 필요성 증가

* **배치 처리 (Batch Processing):** 데이터를 모아서 일정 주기로 한꺼번에 처리하는 방식 (예: 정산).
* **스트림 처리 (Stream Processing):** 실시간으로 들어오는 이벤트를 연속적으로 처리하여 즉각적인 결과를 도출.

### 단일 서버의 확장성 부족

* 기존 단일 서버 환경에서는 대규모 트래픽이나 데이터 처리에 한계가 있음.
* **예시:** 나이키(Nike) 온라인 쇼핑몰 70% 할인 행사 시 트래픽 폭주로 인한 서버 다운 등, 단일 서버로는 감당하기 힘든 상황 발생.

### 기존 데이터 처리 방식(Hadoop MapReduce)의 한계

* **디스크 기반 처리 속도 문제:** Spark 이전 기술(Hadoop)은 데이터 처리 중간 결과를 디스크(Disk)에 저장하고 다시 읽어오는 방식을 사용.
* 디스크는 메모리(RAM)보다 읽기/쓰기 속도가 현저히 느려, 전체적인 데이터 처리 속도 저하 발생.

## 2. Spark란 무엇인가?

### Spark의 정의 및 특징

* **General Unified Engine:** (2014년 이후) Hadoop MapReduce의 단점을 보완하고, 다양한 작업(배치, 스트림, ML 등)을 하나의 엔진에서 처리할 수 있는 통합 엔진.
* **Hadoop 생태계와의 관계:** HDFS, YARN 등의 하둡 생태계 위에서 분석과 처리를 담당하는 핵심 엔진으로 Spark가 주로 사용됨.

### Spark의 문제 해결 방식 (vs Hadoop)

1. **메모리 기반 연산 (In-Memory Computing):** 디스크 I/O를 최소화하여 처리 속도 비약적 향상.
2. **DAG (Directed Acyclic Graph) 기반 스케줄링:** 작업의 순서와 의존성을 그래프로 그려 병렬 처리를 최적화.
3. **Tungsten 엔진:** 코드 생성 최적화를 통해 성능 향상.

### Spark 설계 철학

* **속도 (Speed):** In-Memory 연산, DAG 스케줄링.
* **사용 편의성:** Java, Scala, Python, R 등 다양한 언어 지원. RDD, DataFrame, Dataset과 같은 고수준 API 제공.

### Spark 아키텍처 스택

* **Spark Core:** 기본 엔진.
* **상위 라이브러리:**
* Spark SQL (Structured Data)
* Spark Streaming (Real-time)
* MLlib (Machine Learning)
* GraphX (Graph Processing)


* **스케줄러 (Cluster Managers):** Standalone, YARN, Mesos.

### Spark 활용 시 주의점

* **엄밀한 실시간 처리 불가:** Micro-batch(작은 단위의 배치) 기반이므로 밀리세컨드(ms) 단위의 초저지연 실시간 처리는 아님.
* **작은 데이터 비효율성:** 분산 처리를 위한 오버헤드가 있어 작은 데이터에는 부적합.
* **자체 파일 관리 시스템 부재:** HDFS, S3 등 외부 저장소 필요.
* **높은 메모리 비용:** 인메모리 방식이므로 RAM 자원을 많이 소모.

---

## 3. Spark의 실행 구조 (Execution Architecture)

### 애플리케이션 구성 요소

1. **클러스터 매니저 (Cluster Manager):** 리소스(CPU, 메모리) 관리.
2. **드라이버 (Driver):** `main()` 함수 실행, `SparkContext` 생성, 애플리케이션의 라이프사이클 관리, 작업을 Task로 변환하여 Executor에 전달.
3. **실행기 (Executor):** 실제 작업을 수행하고 데이터를 저장(Cache)하는 워커 노드의 프로세스.
4. **잡 (Job):** 액션(Action)이 발생할 때 생성되는 작업 단위.
5. **스테이지 (Stage):** 셔플(Shuffle, 데이터 이동)을 기준으로 나뉘는 실행 단위.
6. **태스크 (Task):** 실행의 가장 작은 단위, 각 파티션에 할당됨.

### Spark Session

* Spark 2.0부터 도입된 통합 진입점.
* 기존의 `SparkContext`, `SQLContext` 등을 캡슐화하여 사용자가 쉽게 DataFrame, SQL 등을 사용할 수 있게 함.

### 연산의 종류 (Operations)

Spark의 연산은 크게 **Transformation**과 **Action**으로 나뉩니다.

#### 1. Transformation (트랜스포메이션)

* **특징:** 즉시 실행되지 않고 실행 계획(Lineage)만 기록함 (**Lazy Evaluation**).
* **Narrow Transformation:** 파티션 간 데이터 이동(Shuffle)이 없음.
* *예시:* `filter()`, `map()`, `coalesce()`
* * **Wide Transformation:** 파티션 간 데이터 이동(Shuffle)이 발생함. 스테이지를 나누는 기준이 됨.


* *예시:* `groupByKey()`, `reduceByKey()`, `join()`



#### 2. Action (액션)

* **특징:** 실제 연산을 트리거하고 결과를 드라이버로 가져오거나 저장함.
* *예시:* `collect()`, `count()`, `save()`, `show()`

### Lazy Evaluation (지연 연산)

* Transformation은 즉시 실행되지 않고, **Action이 호출되는 시점**에 전체 DAG를 분석하여 최적화된 실행 계획을 수립 후 실행.
* **장점:** 불필요한 연산 생략 가능, 장애 발생 시 Lineage를 통해 데이터 복구 가능(내구성).

---

## 4. Spark 설치 및 환경 설정 (Code & Command)

### WSL (Windows Subsystem for Linux) 환경 설치 예시

**1. Spark 다운로드 및 압축 해제**

```bash
wget https://archive.apache.org/dist/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz
tar -xvzf spark-3.5.4-bin-hadoop3.tgz
sudo mv spark-3.5.4-bin-hadoop3 spark

```

**2. 환경 변수 설정 및 실행 확인**
*(환경 변수 설정 후)*

```bash
# Spark 실행 확인
spark-shell

# 종료 명령어
:quit

```

---

## 5. Pyspark 코드 예제 (Code Examples)

### 1. 간단한 Pyspark 실행 및 연산

`pyspark` 쉘 또는 Python 스크립트 내부에서의 동작 방식입니다.

```python
# SparkContext 및 SparkSession 설정 (일반적으로 쉘에서는 자동 생성됨)
# Python version 3.12.3
# SparkContext available as 'sc'
# SparkSession available as 'spark'

>>> a = 10
>>> b = 50
>>> print("a+b=", a+b)
a+b= 60

```

### 2. Pyspark 내부 동작 코드 (스크립트 형태)

실제 애플리케이션 작성 시의 구조입니다.

```python
from pyspark.sql import SparkSession

# SparkSession 생성 (Builder 패턴)
spark = SparkSession.builder.appName("App").getOrCreate()

# Spark 버전 출력
print(spark.version)
# 결과: 3.5.4

# Spark 세션 종료
spark.stop()

```

### 3. `sc.textFile()`을 활용한 파일 읽기 (RDD)

텍스트 파일을 읽어 RDD로 변환하고 데이터를 확인하는 예제입니다.

```python
# 1. 파일 로드 (RDD 생성)
>>> rdd = sc.textFile("file:///usr/local/spark/data/test.txt")

# 2. 현재 파티션 개수 확인
>>> rdd.getNumPartitions()
2
>>> print("현재 파티션 개수: ", rdd.getNumPartitions())

# 3. collect() 함수로 데이터 확인 (Action 연산)
# 주의: 큰 데이터셋에서는 드라이버 메모리 초과 위험으로 사용 지양
>>> result = rdd.collect()
>>> print(result)
['Hello Spark', 'Apache Spark is powerful', 'Big Data Processing']

```

### 4. `filter()` 연산 (Transformation)

특정 키워드가 포함된 줄만 걸러내는 예제입니다.

```python
# "Spark"라는 단어가 포함된 라인만 필터링
# filter()는 Transformation이므로 즉시 실행되지 않고 새로운 RDD를 정의함
>>> filtered_rdd = rdd.filter(lambda line: "Spark" in line)

# foreach()는 Action 연산으로 실제 출력을 수행
>>> filtered_rdd.foreach(print)

# 출력 결과
Hello Spark
Apache Spark is powerful

```

---

## 6. Docker를 활용한 Spark 실행

### Dockerfile 예시

Spark 실행을 위한 도커 이미지 빌드 파일입니다.

```dockerfile
FROM apache/spark:3.5.4

USER root
# 필요한 파이썬 패키지 설치 (예: pandas)
RUN python3 -m pip install --no-cache-dir pandas==2.0.3

USER spark

```

### Docker 환경에서 DataFrame 생성 예제

`docker-compose.yaml` 등을 통해 구성된 환경에서 실행되는 코드입니다.

```python
from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .appName("Example") \
    .getOrCreate()

# 간단한 데이터 생성
data = [
    ("Alice", 20),
    ("Bob", 30),
    ("Cathy", 40)
]
columns = ["name", "age"]

# DataFrame 생성
df = spark.createDataFrame(data, columns)

# 결과 출력 (Action)
df.show()

# 출력 결과 테이블
# +-----+---+
# | name|age|
# +-----+---+
# |Alice| 20|
# |  Bob| 30|
# |Cathy| 40|
# +-----+---+

spark.stop()

```

---
