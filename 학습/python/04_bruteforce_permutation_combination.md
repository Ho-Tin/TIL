# 완전탐색/순열/조합/부분집합/비트연산

## 1. 완전탐색(Brute Force)
- 가능한 모든 경우의 수를 시도하여 정답을 찾는 방법
- 작은 입력에 적합, 시간복잡도 급격히 증가
- 예시: 비밀번호 맞추기, 모든 경로 탐색 등
- 예시 코드:
```python
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            print(i, j)
```

## 2. 순열(Permutation)
- N개 중 R개를 순서 있게 뽑는 경우의 수 (중복X)
- itertools.permutations, DFS 직접구현 등
- 예시:
```python
from itertools import permutations
for p in permutations([1,2,3], 2):
    print(p)
```
- DFS 직접구현:
```python
def perm(arr, r, path=[]):
    if len(path) == r:
        print(path)
        return
    for i in arr:
        if i not in path:
            perm(arr, r, path + [i])
perm([1,2,3], 2)
```

## 3. 조합(Combination)
- N개 중 R개를 순서 없이 뽑는 경우의 수 (중복X)
- itertools.combinations, 재귀 직접구현 등
- 예시:
```python
from itertools import combinations
for c in combinations([1,2,3], 2):
    print(c)
```
- 재귀 직접구현:
```python
def comb(arr, r, start=0, path=[]):
    if len(path) == r:
        print(path)
        return
    for i in range(start, len(arr)):
        comb(arr, r, i+1, path + [arr[i]])
comb([1,2,3], 2)
```

## 4. 부분집합(Subset)
- 집합의 모든 부분집합(2^N개) 생성
- 비트마스킹, 재귀 등 다양한 방법
- 예시(비트마스킹):
```python
arr = [1,2,3]
n = len(arr)
for i in range(1 << n):
    subset = [arr[j] for j in range(n) if i & (1 << j)]
    print(subset)
```
- 예시(재귀):
```python
def subset(arr, idx=0, path=[]):
    if idx == len(arr):
        print(path)
        return
    subset(arr, idx+1, path)
    subset(arr, idx+1, path+[arr[idx]])
subset([1,2,3])
```

## 5. 비트연산
- &, |, ^, ~, <<, >> 등, 부분집합 생성, 상태 저장, 집합 연산 등에서 활용
- 예시:
```python
bin(7) # '0b111'
bin(7).count('1') # 3
```

## 6. 실전 팁
- itertools, 재귀, 비트마스킹 등 다양한 구현법을 상황에 맞게 선택
- 입력 크기가 크면 완전탐색은 비효율적, 그리디/DP/분할정복 등 다른 방법 고려
