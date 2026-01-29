

---

# Spark DataFrame과 Spark SQL 정리

## 1. 챕터의 포인트

* **DataFrame과 Spark SQL:** 개념 및 특징 이해
* **DSL과 SQL을 활용한 데이터 처리:** 실제 코드 활용법

## 2. RDD와 DataFrame의 이해

### RDD (Resilient Distributed Dataset)란?

* **정의:** 데이터를 병렬 처리하는 핵심적인 역할을 수행하며 빠르고 안정적으로 동작하는 프로그램을 작성 가능하게 함.
* **한계 (BUT):**
* 데이터 값 자체는 표현 가능하지만, 데이터에 대한 메타 데이터, **'스키마(Schema)'**에 대해 명시적으로 표현할 방법이 없음.



### DataFrame 소개

* **정의:** **스키마(Schema)**를 가진 분산 데이터 컬렉션.
* **특징:**
* 데이터를 행(Row)과 열(Column)로 구성된 **표 형태**로 관리.
* 각 열은 명확한 데이터 타입과 메타 데이터(Schema)를 가지고 있음.
* Spark SQL이 제공하는 구조화된 데이터 모델로서 RDD의 한계를 보완함.



### DataFrame API - 데이터 타입

* **기본 타입:** Byte, Short, Integer, Long, Float, Double, String, Boolean, Decimal
* **정형화 타입:** Binary, Timestamp, Date, Array, Map, Struct, StructField
* **핵심:** 실제 데이터를 위한 스키마를 정의할 때 어떻게 이런 타입들이 연계되는지를 아는 것이 중요.

**[코드 예시: 스키마 정의]**

```python
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("Scores", ArrayType(IntegerType()), True)
])

```

### RDD vs DataFrame 차이점 비교

| 구분 | RDD | DataFrame |
| --- | --- | --- |
| **데이터 구조** | 값만 표현 가능, 스키마 표현 불가능 | 명확한 스키마(컬럼, 데이터 타입)를 가진 구조적 데이터 |
| **최적화** | 최적화가 어려움, 직접적 연산 필요 | **Catalyst Optimizer**를 통한 자동 최적화 및 빠른 처리 가능 |
| **API 수준** | 낮음 (저수준 API) | 높음 (고수준 API, SQL 활용 가능) |

### DataFrame을 사용하는 경우

* 구조화 및 도메인 기반 API가 필요할 때
* 복잡한 연산(filter, map, agg, avg, sum, SQL, columnar access 등)이 필요할 때
* 데이터에 대한 Lambda 식이 필요할 때
* 성능 최적화를 위해 컴파일 시 타입 안전성을 보장하고 싶을 때
* 코드 최적화 및 Tungsten의 효율적인 코드 제너레이션이 필요할 때
* 일관성과 간결함을 원할 때

## 3. Spark SQL의 역할 및 구조

### SQL의 역할

* SQL 같은 질의 수행
* 스파크 컴포넌트들을 통합하고, DataFrame, Dataset이 Java, Scala, Python, R 등 여러 프로그래밍 언어로 정형화 데이터 관련 작업을 단순화할 수 있도록 추상화
* 정형화된 파일 포맷(JSON, CSV, txt, avro, parquet, orc 등)에서 스키마와 정형화 데이터를 읽고 쓰며, 데이터를 임시 테이블로 변환
* 빠른 데이터 탐색을 할 수 있도록 대화형 Spark SQL 쉘 제공
* 표준 데이터베이스 JDBC/ODBC 커넥터를 통해, 외부의 도구들과 연결할 수 있는 중간 역할 제공
* 최종 실행을 위해 최적화된 질의 계획과 JVM을 위한 최적화된 코드를 생성

### 내부 작동 원리 (Catalyst Optimizer)

* **SQL / DataFrames / Datasets** -> **Catalyst Optimizer** -> **Physical Plan** -> **Spark (RDD)**
* **관계:** SQL과 DataFrame API는 서로 완전히 독립된 별개의 것이 아님.
* 둘 다 최적화 엔진(Catalyst Optimizer)을 공유하고, 내부적으로 통합된 구조를 가짐.
* Spark에서는 DataFrame API를 이용해 작성된 데이터 처리 명령을 내부적으로 Spark SQL의 엔진으로 최적화해 실행함.



### Dataset API (참고)

* 스파크 2.0에서 개발자들이 한 종류의 API로 통합하려는 노력의 산물.
* **특징:** 정적 타입(Typed) API와 동적 타입(Untyped) API의 특성을 결합.
* **주의:** Java, Scala는 타입 안전(Type Safe)을 보장하지만, Python, R은 타입 안전을 보장하지 않음.

---

## 4. DSL과 SQL을 활용한 데이터 처리 (상세 코드)

이 섹션에서는 DataFrame을 생성하고 조작하는 DSL(Domain-Specific Language) 방식과 SQL 방식의 코드를 다룹니다.

### 4.1. View 등록 및 SQL 실행 기본

DataFrame을 SQL로 쿼리하기 위해서는 뷰(View)로 등록해야 합니다.

```python
# DataFrame을 뷰로 등록하기
df.createTempView("viewName")
df.createGlobalTempView("viewName")
df.createOrReplaceTempView("viewName")

# 뷰에 SQL 쿼리 실행하기
spark.sql("SELECT * FROM viewName").show()
spark.sql("SELECT * FROM global_temp.viewName").show()

```

### 4.2. DataFrame 생성 (DSL 코드)

**직접 생성 (SparkSession 및 Schema 활용)**

```python
# SparkSession 생성
spark = SparkSession.builder.appName("ExampleApp").getOrCreate()

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# 데이터 전처리 및 DataFrame 생성
# (예: people.txt 파일을 읽어 파싱 후 생성하는 과정)
people_rdd = spark.sparkContext.parallelize(["Mine, 28", "Filip, 29", "Jonathan, 30"])
people_data = people_rdd.map(lambda p: Row(name=p.split(",")[0], age=int(p.split(",")[1])))

df = spark.createDataFrame(people_data, schema)

# 결과 출력
df.show()

```

**파일로부터 생성 (From File)**

```python
# DataFrame 직접 생성 (CSV 예시)
people_df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt") \
    .toDF("name", "age")

# 결과 출력
people_df.show()

```

**다양한 데이터 소스**

```python
# JSON
df = spark.read.json("filename.json")
# 또는
df = spark.read.load("filename.json", format="json")

# Parquet files
df = spark.read.load("filename.parquet")

# TXT files
df = spark.read.text("filename.txt")

```

### 4.3. 데이터 검사 (Inspect Data)

```python
# 처음 n개의 행 반환
df.take(n)

# DataFrame의 스키마 반환
df.schema

# 요약 통계 계산
df.describe().show()

# 열 이름 반환
df.columns

```

### 4.4. 쿼리 (Select) - DSL vs SQL

**기본 조회**

```python
# DSL 방식: column1, column2 선택
df.select("column1", "column2").show()

# SQL 방식: View 등록 후 실행
df.createOrReplaceTempView("my_table")
spark.sql("SELECT column1, column2 FROM my_table").show()

```

**표현식과 필터 (Expressions & Filters)**

```python
# DSL/SQL 혼합 개념: 컬럼 연산 및 별칭(Alias)
# column2에 1을 더해 column2_plus1로 명명
spark.sql("SELECT column1, column2 + 1 AS column2_plus1 FROM my_table").show()

# 조건 필터 (WHERE 절)
# column2가 100보다 큰 데이터 필터링
spark.sql("SELECT * FROM my_table WHERE column2 > 100").show()

```

### 4.5. 조건문 및 문자열 처리 (SQL 코드 위주)

**조건문 (CASE WHEN)**

```python
# column2가 100보다 크면 1, 아니면 0으로 표시해 새로운 컬럼 'flag' 생성
spark.sql("""
    SELECT column1, 
    CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag 
    FROM my_table
""").show()

# 특정 값 필터링 (IN)
# column1 값이 'A' 또는 'B'인 행만 필터링
spark.sql("SELECT * FROM my_table WHERE column1 IN ('A', 'B')").show()

```

**문자열 조건 처리 (LIKE, STARTSWITH, ENDSWITH)**

```python
# 'A'로 시작하는 문자열 (LIKE 'A%')
spark.sql("SELECT column1, column1 LIKE 'A%' AS starts_with_A FROM my_table").show()

# '00'으로 끝나는 경우 (LIKE '%00')
# CAST를 사용하여 숫자를 문자열로 변환 후 비교 예시
spark.sql("SELECT column2, CAST(column2 AS STRING) LIKE '%00' AS ends_with_00 FROM my_table").show()

# 정확히 일치하는 경우
spark.sql("SELECT column1, column1 = 'A' AS is_A FROM my_table").show()

```

**문자열 추출 및 범위 조건 (Substring, Between)**

```python
# 문자열 추출 (SUBSTRING)
# column1에서 2번째 문자부터 3개의 문자를 추출하여 컬럼 이름을 'sub'로 저장
spark.sql("SELECT SUBSTRING(column1, 2, 3) AS sub FROM my_table").show()

# 범위 조건 (BETWEEN)
# column2 값이 50~150 사이에 있으면 TRUE 표시
spark.sql("SELECT column1, column2, column2 BETWEEN 50 AND 150 AS is_between_50_150 FROM my_table").show()

```

### 4.6. 컬럼 변경, 삭제 및 집계

**컬럼 이름 변경 및 삭제**

```python
# 컬럼 이름 변경 (Alias)
# column1 -> alphabet, column2 -> number
spark.sql("SELECT column1 AS alphabet, column2 AS number FROM my_table").show()

# 컬럼 삭제 효과 (원하는 컬럼만 선택)
spark.sql("SELECT column2 FROM my_table").show()

```

**그룹화 및 카운트 (Group By, Count)**

```python
# column1을 기준으로 그룹화하고 각 그룹의 개수를 계산하여 출력
spark.sql("""
    SELECT column1, count(*) as count 
    FROM my_table 
    GROUP BY column1
""").show()

```

**정렬 (Ordering)**

```python
# column1 오름차순, column2 내림차순 정렬
spark.sql("""
    SELECT column1, column2 
    FROM my_table 
    ORDER BY column1 ASC, column2 DESC
""").show()

```

**결측치 처리 (Missing & Replacing Values)**

```python
# NULL 값 대체 (Coalesce / NVL 개념)
# column2의 NULL -> 0으로 대체
spark.sql("SELECT column1, coalesce(column2, 0) FROM my_table").show()

# NULL 제거
# column2에 값이 있는 경우만 선택
spark.sql("SELECT * FROM my_table WHERE column2 IS NOT NULL").show()

# 문자열 NULL 대체
# column1이 NULL이면 'Alpha'로 대체 (NVL 유사 기능)
spark.sql("SELECT nvl(column1, 'Alpha') FROM my_table").show()

```