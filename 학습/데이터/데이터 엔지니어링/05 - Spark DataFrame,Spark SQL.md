
---

# Spark SQL & DataFrame 완벽 정리

## 1. 핵심 개념: RDD와 DataFrame

### 1.1. RDD (Resilient Distributed Dataset)

* **정의:** Spark의 가장 기본적인 데이터 단위로, 분산 처리를 위한 핵심 역할을 수행.
* **한계 (Why DataFrame?):** 데이터 값 자체는 표현할 수 있지만, 데이터의 구조(**Schema**)를 명시적으로 표현하지 못함. 최적화가 어렵고 코드가 복잡해질 수 있음.

### 1.2. DataFrame

* **정의:** **스키마(Schema)**를 가진 분산 데이터 컬렉션.
* **특징:**
* **구조화:** 행(Row)과 열(Column)로 구성된 테이블 형태.
* **최적화:** **Catalyst Optimizer**를 통해 내부적으로 실행 계획을 자동 최적화.
* **유연성:** SQL 쿼리와 도메인별 언어(DSL)를 모두 지원.



### 1.3. RDD vs DataFrame 비교

| 구분 | RDD | DataFrame |
| --- | --- | --- |
| **데이터 표현** | 값(Value)만 존재 (비구조적) | **스키마(Schema)**를 가진 구조적 데이터 |
| **최적화** | 개발자가 직접 최적화 필요 | **Catalyst Optimizer**가 자동 최적화 |
| **API 레벨** | Low-level (복잡함) | High-level (SQL, DSL 사용 가능) |
| **성능** | 상대적으로 느림 (Python 사용 시 오버헤드 큼) | 빠름 (Tungsten 엔진, 언어 간 성능 차이 적음) |

---

## 2. Spark SQL 내부 동작 원리 (Catalyst Optimizer)

Spark는 사용자가 **SQL**을 쓰든 **DataFrame DSL**을 쓰든 내부적으로는 동일하게 처리됩니다.

> **처리 흐름:**
> SQL / DataFrame API 코드 작성
> ⬇
> **Catalyst Optimizer** (논리적 계획 수립 및 최적화)
> ⬇
> Physical Plan (물리적 실행 계획 생성)
> ⬇
> **RDD 연산으로 변환되어 실행**

---

## 3. 데이터 처리 실전 (SQL vs DSL)

영상에 나온 SQL 예제를 Python 개발 환경(PySpark)에서 주로 사용하는 **DSL 방식**으로 변환하여 비교 정리했습니다.

**[사전 준비]**

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, lit, when

# SparkSession 생성
spark = SparkSession.builder.appName("SparkCourse").getOrCreate()

```

### 3.1. 데이터 조회 및 연산 (Select & Expressions)

SQL은 `SELECT` 절에 연산을 적지만, DSL은 `select()` 안에 `col()` 객체를 사용하여 연산합니다.

* **기능:** 특정 컬럼 선택 및 값 변경(더하기)
* **SQL:** `SELECT column1, column2 + 1 AS col2_plus FROM table`

```python
# DSL (PySpark)
df.select(
    col("column1"),
    (col("column2") + 1).alias("col2_plus")  # 컬럼 연산 후 별칭 지정
).show()

```

### 3.2. 조건 필터링 (Filter)

* **기능:** 특정 조건에 맞는 행만 추출 (`WHERE`)
* **SQL:** `SELECT * FROM table WHERE column2 > 100`

```python
# DSL (PySpark)
df.filter(col("column2") > 100).show()

```

### 3.3. 조건문 (Case When)

복잡한 `CASE WHEN` 구문은 PySpark의 `when().otherwise()` 체인으로 직관적으로 구현 가능합니다.

* **기능:** 조건에 따라 다른 값을 부여하여 새 컬럼 생성
* **SQL:**
```sql
SELECT CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag FROM table

```



```python
# DSL (PySpark)
df.select(
    col("column1"),
    F.when(col("column2") > 100, 1)  # 조건 만족 시 1
     .otherwise(0)                   # 아니면 0
     .alias("flag")
).show()

```

### 3.4. 문자열 처리 (String Operations)

* **기능:** 문자열 포함 여부, 자르기 등
* **SQL:**
* `LIKE 'A%'` (A로 시작)
* `SUBSTRING(col, 2, 3)` (문자열 자르기)



```python
# DSL (PySpark)

# 1. 시작 문자열 확인 (StartsWith)
df.filter(col("column1").startswith("A")).show()

# 2. 특정 값 포함 여부 (IN)
df.filter(col("column1").isin("A", "B")).show()

# 3. 문자열 자르기 (Substring)
# (SQL과 달리 인덱스 시작 위치 주의 필요, PySpark substr은 1-based index)
df.select(
    col("column1").substr(2, 3).alias("sub_string")
).show()

```

### 3.5. 그룹화 및 집계 (Aggregation)

* **기능:** 그룹별 데이터 개수 세기 (`GROUP BY`)
* **SQL:** `SELECT column1, count(*) FROM table GROUP BY column1`

```python
# DSL (PySpark)
df.groupBy("column1").count().show()

```

### 3.6. 정렬 (Sorting)

* **기능:** 다중 컬럼 정렬 (`ORDER BY`)
* **SQL:** `ORDER BY column1 ASC, column2 DESC`

```python
# DSL (PySpark)
df.orderBy(
    col("column1").asc(),
    col("column2").desc()
).show()

```

### 3.7. 결측치 처리 (Handling NULL)

데이터 전처리 과정에서 가장 빈번하게 사용되는 기능입니다.

* **기능:** NULL 값을 0으로 대체 (`COALESCE` / `NVL`)
* **SQL:** `SELECT coalesce(column2, 0) FROM table`

```python
# DSL (PySpark)

# 방법 1: fillna 사용 (전체 적용 혹은 특정 컬럼 적용)
df.fillna(0, subset=["column2"]).show()

# 방법 2: coalesce 함수 사용 (컬럼 단위 연산 시)
df.select(F.coalesce(col("column2"), lit(0))).show()

```

---

## 4. 요약: 언제 무엇을 써야 할까?

| 방식 | 추천 상황 | 비고 |
| --- | --- | --- |
| **DSL (DataFrame API)** | **[권장]** 일반적인 데이터 파이프라인 개발 시 | 컴파일 타임에 문법 오류 발견 용이, 코드 자동 완성 지원, Pythonic한 코드 작성 가능. |
| **Spark SQL** | 복잡한 쿼리 마이그레이션, 분석가(Analyst)와의 협업 시 | 기존 SQL 쿼리를 그대로 재사용할 때 유리. 하지만 런타임에 오류가 발견될 수 있음. |

**Tip:** 최신 PySpark 개발 트렌드는 가독성과 디버깅 용이성을 위해 **DSL(DataFrame API)** 사용을 지향합니다.