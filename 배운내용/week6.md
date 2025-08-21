## 250819
### 완전탐색 : 답이 될 수 있는 모든 경우를 시도해보는 알고리즘
- 순열, 조합, 부분집합
- Baby-gin Game
- 순열 : 모든 경우의 수( 순서 중요함)
- 조합 : 모든 경우의 수( 순서 x ex: 로또)
  - 탐욕 알고리즘(Greedy) : 최적이라고 생각되는 것을 선택해 나가는 방식
  - 분할 정복(Divide and Conquer) : 복잡한 문제를 더 작은 하위 문제들로 나누는 방식 
  - 다이나믹 프로그래밍(Dynamic Programming, DP) : 과거의 데이터를 이용하여 현재의 데이터를 만들어내는 방식
- 완전탐색
  - 모든 경우의 수를 나열해보고 확인
  - 대부분 문제에 적용이 가능하다
  - 경우의 수가 작다면 유리(시간이 오래걸림)
  - 최적화가 별로임
- 순열
  - 시간 복잡도 : N!
  - n,
```
from itertools import permutations #<< 순열 딸깍
permutations(변수)
```
## 250820
- 조합
  - nCr
  - 시간 복잡도 : n! / (n-r)!r!
```
# 공식
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
```
import itertools # 반복문 딸깍 import
from itertools import
itertools.permutations(변수) #<< 순열 딸깍
itertools.combinations(변수, 조합숫자) # 조합 딸깍
itertools.product(변수, repeat=조합숫자) # 중복순열
itertools.combinations_with_replacement(변수, 조합숫자) # 중복조합
```
## 250821
- 부분집합
- 집합이 포함딘 원소들을 선택하는 것
- 원소들의 그룹에서 최적의 부분 집합을 찾는데 사용
- 배낭 짐싸기(knapsack)
- 시간 복잡도 : 2n
