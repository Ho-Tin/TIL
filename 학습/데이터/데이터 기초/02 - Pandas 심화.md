업로드해주신 "Pandas 심화" 강의 동영상을 분석하여, 주요 내용과 코드를 상세하게 정리한 Markdown 문서입니다. 요청하신 대로 코드 부분은 요약 없이 슬라이드에 나온 내용을 그대로 포함하였습니다.

---

# Pandas 심화 학습 정리

이 문서는 SSAFY(Samsung Software Academy for Youth)의 Pandas 심화 강의 내용을 기반으로 작성되었습니다.

## 1. Pandas와 NumPy 비교

### Pandas

* **주요 용도:** 2차원 데이터(표 형태, DataFrame)를 다룰 때 유용
* **특징:**
* 데이터 분석, 전처리, 조작이 편리함
* 엑셀, CSV, SQL 결과 같은 표 형식의 데이터 처리에 최적화되어 있음



### NumPy

* **주요 용도:** 다차원 배열(1D, 2D, 3D 이상)을 다루는데 특화됨
* **특징:**
* 특히 딥러닝과 고성능 연산을 위해 주로 사용됨
* 3차원 이상 데이터(이미지, 시계열, 텐서 연산 등) 처리에 적합함



---

## 2. NumPy의 ndarray

### ndarray 개요

* **정의:** N 차원(Dimension) 배열(Array) 객체
* **구조:** 1차원(Vector), 2차원(Matrix), 3차원(Tensor) 등의 구조를 가짐

### ndarray 생성 및 속성

#### 1) `arange()`: 순차적 생성

0부터 지정된 숫자까지 순차적으로 생성합니다.

```python
import numpy as np

sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype)
print(sequence_array.shape)
print(type(sequence_array))

# 출력 결과
# [0 1 2 3 4 5 6 7 8 9]
# int32
# (10,)
# <class 'numpy.ndarray'>

```

#### 2) `zeros()` / `ones()`: 초기화 생성

shape와 dtype을 지정하여 0 또는 1로 채워진 배열을 생성합니다.

```python
# zeros 생성
zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
# 출력:
# [[0 0]
#  [0 0]
#  [0 0]]

# ones 생성
ones_array = np.ones((3, 2), dtype='int32')
print(ones_array)
# 출력:
# [[1 1]
#  [1 1]
#  [1 1]]

```

#### 3) 형태(shape)와 차원(ndim)

* **형태:** `ndarray.shape` 속성 (예: `(3,)`, `(2, 3)`)
* **차원:** `ndarray.ndim` 속성 (예: `1차원`, `2차원`)

#### 4) Axis(축)의 이해

* **1차원:** axis 0 (열 방향)
* **2차원:** axis 0 (행 방향, ↓), axis 1 (열 방향, →)
* **3차원:** axis 0 (깊이/높이), axis 1 (행), axis 2 (열)

#### 5) `reshape()`: 차원과 크기 변경

차원을 변경할 때, 전체 데이터 개수(Size)가 맞지 않으면 `ValueError`가 발생합니다.

```python
array1 = np.arange(10)
print('array1:\n', array1)

# (2, 5)로 reshape
array2 = array1.reshape(2, 5)
print('array2:\n', array2)

# (5, 2)로 reshape
array3 = array1.reshape(5, 2)
print('array3:\n', array3)

# 오류 발생 예시 (10개 데이터를 4x3=12 공간에 넣으려 할 때)
# array1.reshape(4, 3) # ValueError 발생

```

---

## 3. Pandas 데이터 구조 및 변환

### 데이터 구조

* **Series:** 1차원을 다루며, 한 종류의 데이터 목록으로 모든 값이 같은 타입.
* **DataFrame:** 2차원을 다루며, 각 열(Column)의 데이터 타입이 다를 수 있음. 크기를 자유롭게 조절 가능.

### 상호 변환 (DataFrame ↔ NumPy/List/Dict)

| 변환 형태 | 설명 |
| --- | --- |
| **DataFrame → List** | `values` 속성으로 ndarray 변환 후 `tolist()` 사용 |
| **DataFrame → NumPy** | `values` 속성 이용 또는 `df.to_numpy()` |
| **DataFrame → Dictionary** | `to_dict()` 메서드 이용 (`to_dict('list')` 등) |

---

## 4. 데이터 처리 (Data Processing)

### 객체 생성

#### 1) `date_range` 및 Series/DataFrame 생성

```python
import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
# 출력 예: DatetimeIndex(['2013-01-01', ...], dtype='datetime64[ns]', freq='D')

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

```

#### 2) 딕셔너리를 이용한 생성

```python
df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo"
})
print(df2)
print(df2.dtypes) # 각 컬럼별 데이터 타입 확인

```

### 데이터 확인 및 선택

#### 1) NumPy로 변환 및 Transpose

```python
# NumPy 배열로 변환
df_to_numpy = df.to_numpy()
print(df_to_numpy)

# Transpose (행/열 전환)
print(df.T)

```

#### 2) Label을 활용한 선택

```python
# 특정 컬럼 선택 (Series 반환)
print(df["A"])

# Slicing을 사용한 행 추출
print(df[0:3]) # 0번째부터 2번째 행까지
print(df["20130102":"20130104"]) # 인덱스 라벨로 범위 지정

```

#### 3) `reindex`: 새로운 행/열 구성

원하는 인덱스/컬럼 순서로 재배치하거나 존재하지 않는 라벨을 추가(NaN 처리)하여 새로운 DataFrame 생성.

```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0]:dates[1], "E"] = 1
print(df1)

```

---

## 5. 데이터 정렬 및 집계

### 정렬 (`sort_values`)

```python
# 'b' 컬럼 기준 오름차순 정렬
titanic_sorted = titanic.sort_values(by=['Name'])
titanic_sorted.head(3)

# 여러 컬럼 기준 내림차순 정렬
titanic_sorted = titanic.sort_values(by=['Pclass', 'Name'], ascending=False)
titanic_sorted.head(3)

```

### 집계 (Aggregation)

`sum()`, `max()`, `min()`, `count()`, `mean()` 등을 사용합니다.

```python
# 전체 count 확인
titanic.count()

# 특정 컬럼 평균
titanic[['Age', 'Fare']].mean()

# 전체 합계
titanic[['Age', 'Fare']].sum()

```

---

## 6. 데이터 가공 (GroupBy & Apply)

### `groupby()`

동일한 컬럼 값을 기준으로 데이터를 그룹화하여 집계함수를 적용합니다.

```python
# Pclass 별 Age의 최대값
titanic.groupby('Pclass')['Age'].max()

# Pclass 별 Age의 최소값
titanic.groupby('Pclass')['Age'].min()

# agg()를 활용하여 여러 함수 동시 적용
titanic.groupby('Pclass')['Age'].agg(['max', 'min'])

```

### `apply()`

Lambda 식이나 사용자 정의 함수를 결합하여 데이터를 일괄적으로 가공합니다.

```python
# 이름의 길이를 계산하여 새로운 컬럼 생성
titanic['Name_len'] = titanic['Name'].apply(lambda x: len(x))
titanic[['Name', 'Name_len']].head()

# 나이(Age)에 따라 카테고리 분류 함수 정의
def categorize_age(age):
    if age <= 5: return 'Baby'
    elif age <= 12: return 'Child'
    elif age <= 18: return 'Teenager'
    elif age <= 25: return 'Student'
    elif age <= 35: return 'Young Adult'
    elif age <= 60: return 'Adult'
    else: return 'Elderly'

# 적용 및 확인
titanic['Age_cat'] = titanic['Age'].apply(categorize_age)
titanic[['Age', 'Age_cat']].head()

```

---

## 7. 데이터 병합 및 변환

### 데이터 병합 (Concat, Merge, Join)

#### 1) `concat`: 붙이기

축(axis)을 기준으로 단순히 데이터를 이어 붙입니다.

```python
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7']})

# 행 방향 병합 (위아래)
result = pd.concat([df1, df2], axis=0)

```

#### 2) `merge`: 병합 (SQL Join과 유사)

공통된 키(Key)를 기준으로 데이터를 병합합니다.

* **Outer Merge:** 키의 합집합 기준
* **Left Merge:** 왼쪽 데이터프레임 키 기준

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# key 컬럼을 기준으로 병합
pd.merge(left, right, on='key')

```

#### 3) `join`: 인덱스 기준 병합

```python
# 기본적으로 인덱스를 기준으로 병합 (how='left' 기본값)
df1.join(df2)

# 접미사(suffix) 사용 (컬럼명 중복 시 처리)
pd.merge(df1, df2, on='key', how='inner', suffixes=('_left', '_right'))

```

#### 4) 불필요한 열 제거

```python
# axis=1 은 열 방향 제거
df_merged.drop(['key', 'C'], axis=1)

```

### 데이터 변환 (Replace, Pivot)

#### 1) `replace()`: 값 치환

```python
# 성별 컬럼 값을 숫자로 변경 (male: 0, female: 1)
# inplace=True를 쓰면 원본 데이터 변경
titanic['Sex'] = titanic['Sex'].replace({'male': 0, 'female': 1})

```

#### 2) `pivot()` vs `pivot_table()`

데이터 형태를 재배치(Reshape)합니다.

* **`pivot()`**: 중복된 값이 없을 때 사용. 단순히 인덱스, 컬럼, 값을 지정하여 재배치.
* **`pivot_table()`**: 중복된 값이 있을 경우 `aggfunc` (평균, 합계 등)을 사용하여 값을 요약하면서 재배치.

```python
# pivot 예시 (사용법 개념)
pivot_df = titanic.groupby(['Sex', 'Pclass'])['Age'].mean().reset_index()
pivot_table = pivot_df.pivot(index='Sex', columns='Pclass', values='Age')

# pivot_table 예시 (바로 집계 가능)
# 성별(Sex) x 객실등급(Pclass) 별 평균 나이(Age)
titanic.pivot_table(index='Sex', columns='Pclass', values='Age', aggfunc='mean')

```

---
