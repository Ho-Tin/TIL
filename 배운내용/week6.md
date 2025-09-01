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

# 250901
## Template system
### Django Template Language (DTL)
    - 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
    - {{변수}}을 사용하여 변수값을 불러올수있다 context
    - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
- Variable(변수.변수)
  - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
  - dot('.')을 이용하여 변수 속성에 접근가능
- Filters(변수 | 함수)
  - 표시할 변수를 수정할 때 사용
- Tags(% 변수 %)
  - 반복 또는 논리(for,if문)을 수행할때 사용
- Comments(# 내용 #)
  - DTL에서 사용하는 주석
 
### 템플릿 상속
- 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축한다
- 'extends'tag
  - 자식 템플리싱 부모 템플릿으로 부터 확장하는것을 의미
- 'block' tag
  - 하위 템플릿에서 재정의 할수 있는 블록을 정의
### 요청과 응답
- HTML 'form' tag
  - 데이터를 보내고 가져오기
  - HTTP 요청을 서버에 보내는 가장 편리한 방법
- 'form' element
  - 사용자로부터 할당된 데이터를 서버로 전송하는것
- 'action' & 'method'
- action
  - 전송될 URL을 지정(목적지)
  - 만약 이 속성을 지정하지 않으면 현재 페이지의 URL로 보내짐
- method
  - 어떤 방식으로 보낼 것인지 정의
  - (GET, POST)를 지정
- input element
  - 사용자의 데이터를 입력 받을 수 있는 요소
  - 속성 값에 따라
  - 'name' attribute
    - input의 핵심 속성
    - 사용자가 입력한 데이터에 붙이는 이ㄹ,ㅁ
- Quert String Parameters
  - 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
  - key=value&key=value 로 구분됨
- request 객체
  - form으로 전송한 데이터 뿐만 아니라 Django로 둘어오는 모든 요청 관련 데이터가 담겨있음
   request.GET.get("key")
### Django URLs
- URL dispatcher
  - URL 패턴을 정의하고 해당 패턴이 일치하는 view함수를 연결(매핑)
- Variable Routing
  - URL 일부에 변수를 포함시키는 것
  - path('articles/<int:num>/', views.index)
  - '<path_converter:variable_name>'
  - Path converters
    - URL 변수 타입(str ,int 등 5가지)
- App URL mapping
  - 각 앱에 URL을 정의하는 것
- include()
  - 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
- Naming URL patterns
  - URL에 이름을 지정하는 것
  - path 함수의 name 인자를 정의해서 사용
- 
  
