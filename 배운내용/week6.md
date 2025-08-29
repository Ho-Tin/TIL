***

# 완전탐색, 순열·조합·부분집합 정리

## 완전탐색
- **답이 될 수 있는 모든 경우를 시도**하는 알고리즘이다.
- 대부분의 문제에 적용 가능하며, 경우의 수가 작을 때 유리하다.
- 경우의 수가 많아지면 **시간이 오래 걸리고** 최적화가 떨어진다.
- 적용 예: 순열, 조합, 부분집합

***

## 주요 개념
- **순열(Permutation):** 모든 경우의 수(순서 중요)
    - 시간복잡도: $$ N! $$
    - 예시: Baby-gin Game, 숫자 맞추기 게임 등
- **조합(Combination):** 모든 경우의 수(순서 무관, ex: 로또)
    - 시간복잡도: $$ \frac{n!}{(n-r)! r!} $$
- **부분집합(Subset):** 집합에 포함된 원소를 선택해서 여러 그룹을 만듦
    - 시간복잡도: $$ 2^n $$
    - 예시: 최적의 부분집합 찾기(배낭 문제 등)

***

## 관련 알고리즘
- **탐욕(Greedy):** 매 단계 최적이라고 생각하는 값을 선택.
- **분할 정복(Divide and Conquer):** 복잡한 문제를 작은 문제로 분할.
- **동적 프로그래밍(Dynamic Programming, DP):** 과거 결과를 이용하여 현재 결과를 도출.

***

## Python 활용 예시

### 순열 (permutations)
```python
from itertools import permutations
permutations(변수)
```

### 조합 (combinations)
```python
from itertools import combinations
combinations(변수, 조합숫자)
```
직접 구현 예시:
```python
def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n - 1): # 조합
        # for rest in comb(arr[:i] + arr[i+1:], n - 1): # 순열
        # for rest in comb(arr, n - 1): # 중복순열
        # for rest in comb(arr[i:], n - 1): # 중복조합
            result.append([elem] + rest)
    return result

print(comb([1,2,3,4], 4))
```

### 중복순열, 중복조합
```python
import itertools
itertools.product(변수, repeat=조합숫자) # 중복순열
itertools.combinations_with_replacement(변수, 조합숫자) # 중복조합
```

***

## 부분집합과 비트 연산자

### 비트 연산자 종류
- `&` : and  
- `|` : or  
- `^` : xor(같으면 0, 다르면 1)  
- `~` : not(반전)  
- `<<` : 왼쪽 이동  
- `>>` : 오른쪽 이동  

### 부분집합 생성 재귀 예시
```python
def generate_subset(depth, included):
    if depth == len(input_list):
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(cnt_subset)
        return
    included[depth] = False
    generate_subset(depth + 1, included)
    included[depth] = True
    generate_subset(depth + 1, included)

input_list = [1,2,3,4]
subsets = []
generate_subset(0, [False] * len(input_list))
print(subsets)
```

***

## 참고 및 팁
- 재귀는 종료 조건이 필수이며, 파라미터 설정 시에는 **현재 포함할지 말지를 결정할 인덱스와 누적값**을 고려한다.
- **부분집합은 바이너리 카운팅 또는 비트 연산**으로도 구현 가능하다.
- 순열/조합/부분집합 문제를 풀 때는 itertools와 재귀함수를 우선적으로 활용한다.

***

이 내용으로 바로 `.md` 파일을 작성하면 됩니다.

