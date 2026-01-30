
---

# Spark DataFrame & SQL 상세 정리

## 1. 핵심 개념: RDD와 DataFrame

### 1.1. RDD (Resilient Distributed Dataset)

* **정의:** 데이터를 병렬 처리하는 핵심적인 역할을 수행하며 빠르고 안정적인 프로그램 작성을 가능하게 함.
* **한계 (But):** 데이터 값 자체는 표현 가능하지만, 데이터에 대한 메타 데이터인 **'스키마(Schema)'**를 명시적으로 표현할 방법이 없음.

### 1.2. DataFrame

* **정의:** **스키마(Schema)**를 가진 분산 데이터 컬렉션.
* **특징:**
* 데이터를 **행(Row)**과 **열(Column)**로 구성된 표 형태로 관리.
* 각 열은 명확한 데이터 타입과 메타 데이터를 가짐.
* Spark SQL이 제공하는 구조화된 데이터 모델로 RDD의 한계를 보완.



### 1.3. RDD vs DataFrame 차이점

| 구분 | RDD | DataFrame |
| --- | --- | --- |
| **데이터 표현** | 값만 표현 가능 (스키마 X) | 명확한 스키마(컬럼, 타입) 보유 |
| **최적화** | 최적화가 어려움 (직접 연산 필요) | **Catalyst Optimizer**를 통한 자동 최적화 |
| **API 수준** | 낮은 수준 (Low-level) | 높은 수준 (High-level, SQL 활용 가능) |

---

## 2. DataFrame API 및 데이터 타입

### 2.1. 지원 데이터 타입

실제 데이터를 위한 스키마 정의 시 아래 타입들의 연계 방식을 아는 것이 중요합니다.

* **기본 타입:** Byte, Short, Integer, Long, Float, Double, String, Boolean, Decimal
* **정형화 타입:** Binary, Timestamp, Date, Array, Map, Struct, StructField

### 2.2. 스키마 정의 코드 (StructType)

```python
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType

schema = StructType([
    StructField("name", StringType(), True),   # 이름: 문자열
    StructField("Scores", ArrayType(IntegerType()), True) # 점수: 정수형 배열
])

```

---

## 3. Spark SQL 아키텍처 (Catalyst Optimizer)

* **구조:** SQL, DataFrame, Dataset API는 서로 독립된 것이 아니라 내부적으로 통합된 구조를 가집니다.
* **작동 원리:**
1. SQL 또는 DataFrame 코드 작성
2. **Catalyst Optimizer**가 논리적 실행 계획을 수립하고 최적화
3. 물리적 실행 계획(Physical Plan) 생성
4. RDD 연산으로 변환되어 실행



---

---

```python
from pyspark.sql.functions import col, lit, when, coalesce, count, desc, asc
# SQL 사용을 위한 뷰 등록 가정
df.TempView("my_table")
df.createGlobalTempView("my_table")
df.createOrReplaceTempView("my_table")
```

### 1. DataFrame 생성 (Creation)

영상에서는 스키마를 정의하고 데이터를 생성하는 과정이 소개되었습니다.

**SQL/Raw Code (영상 내용)**

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# RDD 혹은 리스트로부터 생성
df = spark.createDataFrame(data, schema)

```

**DSL Code (파일 로드 방식)**

```python
# CSV 파일 읽기 (헤더 있음, 스키마 자동 추론)
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("people.csv")

```

---

### 2. 조회 및 연산 (Select & Expressions)

특정 컬럼을 선택하거나, 값을 계산하여 새로운 컬럼으로 만드는 작업입니다.

#### 2.1. 단순 컬럼 선택

**SQL Code**

```python
spark.sql("SELECT column1, column2 FROM my_table").show()

```

**DSL Code**

```python
df.select("column1", "column2").show()
# 또는
df.select(col("column1"), col("column2")).show()

```

#### 2.2. 컬럼 연산 및 별칭(Alias)

**SQL Code**

```python
# column2에 1을 더해 'column2_plus1' 생성
spark.sql("SELECT column1, column2 + 1 AS column2_plus1 FROM my_table").show()

```

**DSL Code**

```python
df.select(
    col("column1"), 
    (col("column2") + 1).alias("column2_plus1")
).show()

```

---

### 3. 조건 필터링 (Filter / Where)

#### 3.1. 값 비교 (부등호)

**SQL Code**

```python
# column2가 100보다 큰 값 필터링
spark.sql("SELECT * FROM my_table WHERE column2 > 100").show()

```

**DSL Code**

```python
df.filter(col("column2") > 100).show()
# 또는
df.where(col("column2") > 100).show()

```

#### 3.2. 특정 값 포함 여부 (IN)

**SQL Code**

```python
# column1이 'A' 또는 'B'인 행 필터링
spark.sql("SELECT * FROM my_table WHERE column1 IN ('A', 'B')").show()

```

**DSL Code**

```python
df.filter(col("column1").isin("A", "B")).show()

```

---

### 4. 조건문 (Case When)

특정 조건에 따라 값을 다르게 부여하는 로직입니다.

**SQL Code**

```python
# column2가 100보다 크면 1, 아니면 0인 'flag' 컬럼 생성
spark.sql("""
    SELECT column1, 
    CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag 
    FROM my_table
""").show()

```

**DSL Code**

```python
df.select(
    col("column1"),
    when(col("column2") > 100, 1)
    .otherwise(0)
    .alias("flag")
).show()

```

---

### 5. 문자열 처리 (String Operations)

#### 5.1. 시작 문자열 확인 (LIKE 'A%')

**SQL Code**

```python
# column1이 'A'로 시작하는지 확인
spark.sql("SELECT column1, column1 LIKE 'A%' AS starts_with_A FROM my_table").show()

```

**DSL Code**

```python
df.select(
    col("column1"),
    col("column1").startswith("A").alias("starts_with_A")
).show()

```

#### 5.2. 끝 문자열 확인 (LIKE '%00')

영상에서는 숫자를 문자열로 변환(CAST)하는 예시가 포함되어 있습니다.

**SQL Code**

```python
# column2(숫자)를 문자로 바꿔서 '00'으로 끝나는지 확인
spark.sql("""
    SELECT column2, 
    CAST(column2 AS STRING) LIKE '%00' AS ends_with_00 
    FROM my_table
""").show()

```

**DSL Code**

```python
df.select(
    col("column2"),
    col("column2").cast("string").endswith("00").alias("ends_with_00")
).show()

```

#### 5.3. 문자열 자르기 (Substring)

**SQL Code**

```python
# 2번째 글자부터 3글자 추출
spark.sql("SELECT SUBSTRING(column1, 2, 3) FROM my_table").show()

```

**DSL Code**

```python
df.select(
    col("column1").substr(2, 3)
).show()

```

---

### 6. 컬럼 변경 및 삭제 (Update & Remove)

#### 6.1. 컬럼 이름 변경

**SQL Code**

```python
# 조회하면서 이름 변경 (Alias)
spark.sql("SELECT column1 AS alphabet, column2 AS number FROM my_table").show()

```

**DSL Code**

```python
# 원본 DataFrame의 컬럼명 자체를 변경하여 리턴
df.withColumnRenamed("column1", "alphabet") \
  .withColumnRenamed("column2", "number") \
  .show()

```

#### 6.2. 컬럼 삭제 효과

**SQL Code**

```python
# 원하는 컬럼만 선택 (column2만 선택 = column1 삭제 효과)
spark.sql("SELECT column2 FROM my_table").show()

```

**DSL Code**

```python
# 명시적으로 컬럼 삭제
df.drop("column1").show()

```

---

### 7. 집계 및 정렬 (Aggregation & Sorting)

#### 7.1. 그룹화 및 카운트 (Group By)

**SQL Code**

```python
spark.sql("""
    SELECT column1, count(*) as count 
    FROM my_table 
    GROUP BY column1
""").show()

```

**DSL Code**

```python
df.groupBy("column1").count().show()

```

#### 7.2. 정렬 (Order By)

**SQL Code**

```python
# column1 오름차순, column2 내림차순
spark.sql("""
    SELECT column1, column2 
    FROM my_table 
    ORDER BY column1 ASC, column2 DESC
""").show()

```

**DSL Code**

```python
df.orderBy(col("column1").asc(), col("column2").desc()).show()

```

---

### 8. 결측치 처리 (Null Handling)

#### 8.1. Null 값 대체

**SQL Code**

```python
# column2가 Null이면 0으로 대체
spark.sql("SELECT column1, coalesce(column2, 0) FROM my_table").show()

```

**DSL Code**

```python
# fillna 사용 (권장)
df.fillna(0, subset=["column2"]).show()

# 또는 coalesce 사용 (컬럼 연산 시)
df.select(col("column1"), coalesce(col("column2"), lit(0))).show()

```

#### 8.2. Null 제거

**SQL Code**

```python
# column2가 Null이 아닌 행만 선택
spark.sql("SELECT * FROM my_table WHERE column2 IS NOT NULL").show()

```

**DSL Code**

```python
# dropna 사용
df.dropna(subset=["column2"]).show()

```