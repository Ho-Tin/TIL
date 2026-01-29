업로드해주신 동영상 강의 내용을 바탕으로 Apache Spark의 **RDD(Resilient Distributed Datasets)** 개념과 관련 코드를 마크다운(Markdown) 형식으로 정리했습니다.

---

# Spark RDD (Resilient Distributed Datasets) 강의 요약

## 1. RDD란?

**정의**: 대용량 데이터를 분산 처리하고 분석하기 위한 Spark의 기본 데이터 처리 단위

* **Resilient (탄력적인)**: 노드 장애 발생 시 데이터 복구 가능
* **Distributed (분산된)**: 여러 노드에 데이터가 나누어 저장됨
* **Dataset (데이터셋)**: 데이터의 집합
* **구조**: 하나의 RDD(원본 데이터셋)는 여러 개의 Partition(분산된 데이터 파티션)으로 나누어짐 (Partitioning/Sharding)

## 2. RDD의 특징

### 탄력성(Resilient) & 불변성(Immutable)

* **불변성**: RDD는 한 번 생성되면 변경할 수 없음 (Read-only)
* **탄력성**: 어떤 노드(서버)가 장애로 인해 중단되더라도, 계보(Lineage)를 통해 데이터를 다시 계산하여 복구 가능
* *흐름: RDD -> Transformations (map, filter...) -> New RDD*

### 데이터 유형

1. **비정형(Unstructured) 데이터**:
* 고정된 포맷이 없는 텍스트 데이터 (로그 파일 등)
* `sc.textFile()`로 로딩 후 `map`, `filter`, `flatMap` 등으로 가공


2. **정형(Structured) 데이터**:
* 컬럼이 있는 테이블 형태 데이터
* DataFrame 또는 `RDD.map()`으로 가공



---

## 3. 주요 구성 요소 및 코드 예제

강의 화면에 나온 코드를 그대로 정리했습니다.

### 3.1. RDD 생성 및 기본 변환 (Basic Transformation)

**Code Snippet:**

```python
from pyspark import SparkContext

sc = SparkContext("local", "LazyEvalExample")

# 1. 텍스트 데이터 로딩 -> Transformation
rdd = sc.parallelize(["apple", "banana", "spark", "data"])

# 2. 대문자로 바꾸기 -> Transformation
upper_rdd = rdd.map(lambda x: x.upper())

# 3. SPARK가 포함된 문자열만 필터링 -> Transformation
filtered_rdd = upper_rdd.filter(lambda x: "SPARK" in x)

# # 지금까지는 아무것도 실행되지 않음! (Lazy Evaluation)

# 4. 결과 확인 (Action)
result = filtered_rdd.collect()

```

### 3.2. RDD 생성 방법 상세

1. **내부 데이터 이용**:
* Python의 리스트(List)나 Scala의 컬렉션을 RDD로 변환
* 주로 테스트나 작은 데이터를 다룰 때 사용
* `sc.parallelize(["cats", "dogs"])`


2. **외부 파일 이용**:
* 실무에서 주로 사용 (텍스트, CSV, JSON 등)
* `sc.textFile("파일 경로")`



---

## 4. RDD 변환(Transformations) 연산 정리

RDD는 기존 RDD를 변경하지 않고 새로운 RDD를 생성합니다.

| 연산자 | 설명 | 특징 |
| --- | --- | --- |
| **MAP** | 각 요소에 함수를 적용하여 새로운 RDD 반환 | 1:1 변환 (입력 1개 -> 출력 1개) |
| **FLATMAP** | 각 요소에 함수를 적용한 뒤 결과를 평탄화(flatten) | 1:N 변환 가능 (리스트를 풀어서 하나의 레벨로 만듦) |
| **FILTER** | 사용자 함수를 적용하여 반환값이 `true`인 항목만 유지 | 조건에 맞는 데이터 추출 |
| **MAPPARTITIONS** | 파티션 단위로 함수를 적용 | 파티션별로 초기화 작업이 필요할 때 효율적 |
| **KEYBY** | 각 항목에 대해 키(Key)를 생성하여 (Key, Value) 쌍 생성 | `keyBy(f)`: f함수의 결과가 Key가 됨 |
| **GROUPBY** | 특정 기준(Key)으로 데이터를 그룹화 | 셔플링(Shuffling)이 발생할 수 있음 |
| **GROUPBYKEY** | (Key, Value) 쌍의 RDD에서 같은 키를 가진 값들을 그룹화 |  |
| **REDUCEBYKEY** | 같은 키를 가진 값들을 줄여나감(Reduce) | **성능상 유리**: 셔플 전에 로컬에서 먼저 집계(Local Aggregation)를 수행하여 데이터 이동량을 줄임 |
| **JOIN** | 두 RDD에서 같은 키를 가진 요소끼리 결합 |  |
| **UNION** | 두 RDD의 요소를 합침 | 중복된 항목은 제거되지 않음 |
| **DISTINCT** | 중복된 항목을 제거 |  |
| **SAMPLE** | 데이터셋의 일부를 추출 | 통계적으로 의미 있는 근사치 확보 (Big Data 처리 효율) |
| **PARTITIONBY** | 키를 기준으로 파티션을 재분배 |  |

### Word Counting 예제 코드 (GROUPBYKEY 활용)

**Code Snippet:**

```python
words = sc.parallelize(['one', 'two', 'two', 'three', 'three', 'three'])
wordPairsRdd = words.map(lambda w: (w, 1))
wordCounts = wordPairsRdd.groupByKey().map(lambda pair: (pair[0], sum(pair[1])))

print(words.collect())
print(wordPairsRdd.collect())
print(wordCounts.collect())

# 출력 결과 예상:
# words: ['one', 'two', 'two', 'three', 'three', 'three']
# wordPairsRdd: [('one', 1), ('two', 1), ('two', 1), ('three', 1), ('three', 1), ('three', 1)]
# wordCounts: [('one', 1), ('two', 2), ('three', 3)]

```

---

## 5. RDD 액션(Actions) 연산 정리

변환된 RDD 데이터를 메모리로 가져오거나, 저장하거나, 집계하는 연산입니다. (실제 실행 트리거)

| 연산자 | 설명 | 예시 결과 (입력: `[1, 2, 3, 4]`) |
| --- | --- | --- |
| **collect()** | 모든 데이터를 리스트로 반환 | `[1, 2, 3, 4]` |
| **count()** | 전체 요소의 개수 반환 | `4` |
| **reduce()** | 전체 요소를 하나로 결합 (누적 연산) | `10` (1+2+3+4) |
| **sum()** | 모든 항목의 합 반환 | `10` |
| **mean()** | 모든 항목의 평균 반환 | `2.5` |

**Reduce 코드 예시:**

```python
x = sc.parallelize([1, 2, 3, 4])
y = x.reduce(lambda a, b: a + b) 
# 결과 y: 10

```

---

## 6. 강의 외적인 멘트 (강사 전달 사항)

* **건강 관리 강조**: 컨디션 조절을 잘 해야 공부도 잘 된다.
* **일정 안내**:
* **다음 주 월요일**: 과목 평가 및 월말 평가 예정
* **다음 주**: Airflow, ElasticSearch 강의 예정
* 내일 방송에서 다시 만남 (SSAFY 로고 노출)



---

이 자료는 Apache Spark RDD의 핵심 개념인 **불변성, 탄력성**과 **Lazy Evaluation(지연 연산)**의 특징을 이해하고, 주요 **Transformation**과 **Action** 함수들의 차이를 파악하는 데 중점을 두고 있습니다. 추가적으로 궁금한 코드가 있다면 말씀해주세요.