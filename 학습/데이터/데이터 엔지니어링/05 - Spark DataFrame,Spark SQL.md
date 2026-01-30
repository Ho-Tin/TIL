
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

## 4. 데이터 처리 코드 상세 (DSL & SQL)

영상에 소개된 기능별 코드 구현 내용입니다.

### 4.1. DataFrame 생성 (Creation)

**1) 직접 생성 (리스트 + 스키마)**

```python
# RDD 생성 후 DataFrame 변환
people_rdd = spark.sparkContext.parallelize(["Mine, 28", "Filip, 29"])
# (중략: 매핑 로직)
df = spark.createDataFrame(people_data, schema)
df.show()

```

**2) 파일로부터 생성 (Source)**

```python
# CSV 파일 읽기
df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt")

# JSON 파일 읽기
df = spark.read.json("filename.json")

# Parquet 파일 읽기
df = spark.read.load("filename.parquet")

```

### 4.2. 데이터 조회 및 검사 (Inspection)

```python
df.take(n)        # 처음 n개의 행 반환
df.schema         # 스키마 구조 반환
df.describe().show() # 요약 통계(평균, 최소, 최대 등) 계산 및 출력
df.columns        # 열(Column) 이름 리스트 반환

```

### 4.3. 쿼리 및 데이터 선택 (Select)

**1) 컬럼 선택**

```python
# DSL 방식
df.select("column1", "column2").show()

# SQL 방식 (View 등록 필요)
df.createOrReplaceTempView("my_table")
spark.sql("SELECT column1, column2 FROM my_table").show()

```

**2) 표현식(Expression)과 별칭(Alias)**

* 기존 컬럼 값을 조작하여 새로운 컬럼으로 조회.

```python
# column2에 1을 더해 'column2_plus1'이라는 이름으로 출력
spark.sql("SELECT column1, column2 + 1 AS column2_plus1 FROM my_table").show()

```

### 4.4. 데이터 필터링 (Filtering)

**1) 조건 필터 (Where)**

```python
# column2가 100보다 큰 데이터만 조회
spark.sql("SELECT * FROM my_table WHERE column2 > 100").show()

```

**2) 특정 값 포함 여부 (IN)**

```python
# column1이 'A' 또는 'B'인 경우
spark.sql("SELECT * FROM my_table WHERE column1 IN ('A', 'B')").show()

```

### 4.5. 조건문 처리 (Case When)

* 조건에 따라 값을 다르게 부여하여 새로운 컬럼(`flag`) 생성.

```python
# column2가 100보다 크면 1, 아니면 0
spark.sql("""
    SELECT column1, 
    CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag 
    FROM my_table
""").show()

```

### 4.6. 문자열 처리 (String Operations)

**1) 패턴 매칭 (Like, StartsWith, EndsWith)**

```python
# 'A'로 시작하는 문자열 찾기 (LIKE 'A%')
spark.sql("SELECT column1, column1 LIKE 'A%' AS starts_with_A FROM my_table").show()

# '00'으로 끝나는 문자열 찾기 (LIKE '%00')
# 숫자인 경우 문자열로 형변환(CAST) 후 비교
spark.sql("SELECT column2, CAST(column2 AS STRING) LIKE '%00' AS ends_with_00 FROM my_table").show()

```

**2) 문자열 자르기 (Substring)**

```python
# column1의 2번째 글자부터 3글자 추출
spark.sql("SELECT SUBSTRING(column1, 2, 3) FROM my_table").show()

```

### 4.7. 컬럼 변경 및 삭제 (Update & Remove)

* **변경:** `AS`를 사용하여 컬럼명을 변경하여 조회.
* **삭제:** 원하는 컬럼만 `SELECT` 함으로써 삭제 효과를 냄.

```python
# column1 -> alphabet, column2 -> number로 이름 변경
spark.sql("SELECT column1 AS alphabet, column2 AS number FROM my_table").show()

```

### 4.8. 집계 및 정렬 (Aggregation & Sorting)

**1) 그룹화 (Group By)**

```python
# column1 기준으로 그룹화하여 개수(Count) 세기
spark.sql("SELECT column1, count(*) as count FROM my_table GROUP BY column1").show()

```

**2) 정렬 (Order By)**

```python
# column1 오름차순, column2 내림차순 정렬
spark.sql("SELECT column1, column2 FROM my_table ORDER BY column1 ASC, column2 DESC").show()

```

### 4.9. 결측치 처리 (Missing Values)

**1) NULL 대체 (Coalesce / NVL)**

```python
# column2가 NULL이면 0으로 대체
spark.sql("SELECT column1, coalesce(column2, 0) FROM my_table").show()

```

**2) NULL 제거**

```python
# column2가 NULL이 아닌 행만 조회
spark.sql("SELECT * FROM my_table WHERE column2 IS NOT NULL").show()

```