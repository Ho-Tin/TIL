## 250728 - 오전
- python 강의
- default dict
### 고수준 언어(기계어로 바꿔주는 번역기)
- 사람이 읽기 쉽다
- python, java
### 저수준 언어
- 기계어(0101010110),어셈블리어
### 파이썬
- 쉽고 간결한 문법
- 세계적인 규모의 커뮤니티
- 파이썬 프로그램 -> 파이썬 인터프리터 -> 운영 체제
- 표현식(Expression) - 값을 꺼내는 것, 값(value), 평가(Evaluate), 문장(Statement)
### 타입(type)
- 의미 있는 연산과 결과 보장
- 오류 예방과 디버깅 용이
- 개발 생산성과 코드 가독성 향상
### 우선순위
- 1순위 (괄호) 
- 2순위 **
- 3순위 -(음수부호)
- 4순위 *,/,%,등등 부호
- 5순위 (덧셈,뺼셈)
### 코딩 작성 괄호 작성시 도움됨<<
### 변수
- 값을 저장하기 위한 이름
- 할당하다, 재할당하다
### 변수,값 메모리
- 변수는 주소를 저장하는 것
- **int(정수) / 진수로도 표현 가능**
- 2진수(0b) binary
- 8진수(0o) octal
- 16진수(0x) hexadecimal
- **지수 표현**
- e또는 E를 사용한 표현
### float - 유한 정밀도
-  무한대를 저장할수 없기 떄문에 2/3 0.66666666 같이 일정 숫자에서 끊어저 저장 (16~17자에서 끊음)
- 부동소수점 에러<<<
실수를 진수로 변환하는 과정에서 발생하는 에러
- **decimal 모듈**을 사용해 에러 방지
- 실수로 저장하기 때문에 문제가 해결됨
- from decimal import Decimal
### sequence Types
- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
- str, 순서가 있고 변경 불가능한 시퀀스 자료형
- 역슬래시(backslash, \) \n 줄바꿈, 엔터 \t 탭
- f-string (f.{a}{b}{c})
- **인덱싱**
- [0]부터 시작
- **슬라이싱**
- hello
- my_str[2:4] 2이상 4미만  'll'
- my_str[0:5:2] 'hlo' 0이상 5미만 2칸씩 
- my_str[::-1] 'olleh' -1이하 전부
- my_str[-4:-2:-2] '' 진행방향이 다르기떄문에 공백
- 문자열은 불면(변경불가)
- 파이썬 스타일 가이드
- **변수명 짓기 중요**
- 주석
- 코드를 이해하거나 문서화하기 위해
- 다른 개발자나 자신에게 코드의 의도나 동작을 설명하는 데 도움
- **나 자신을 위해** 사용
- python 튜터  render all 모시꺵이 작성
 https://pythontutor.com/python-compiler.html#mode=edit

## 250728 - 오후
- list, dict ,set  
- **list** 
- 순서대로 변경 가능한 시퀀스 자료
- 어떤 자료형도 저장할 수 있음
- list는 가변이다 < 변경할수있다>
- [] 사용
- **tuple**
- list와 비슷하지만 변경 불가능
- () 사용--없어도 됨
- , ex   a = (1, )
-  **range**
- range(0,10) 0이상 10 미만 / 0부터 9까지
### non_시퀀스
- **dict**
- 중복도 없고 순서도 없는 변경 가능한 자료형
- EX 노래방 번호 
- key - Value 
- key는 변경 불가능한 자료형만 사용 가능(str,int,float, tuple,range 등등)
- value는 모든 자료형 사용 가능
- defaultdict(list) << list 에 default로 빈값 지정
- **set**
- 순서와 중복이 없는 변경 가능한 자료형
- 수학에서 **집합**과 동일한 연산
- {}로 표시
```
list = [1,2,3,4,1,1,1,1]
print(list) # 1,2,3,4,1,1,1,1
list = set(list)
print(list) #  1,2,3,4
```
- 합집합 |  myset1 | myset2
- 교집합 &  myset1 & myset2
- 차집합 -
- **None**
- 값이 없음을 의도적으로 표현
- **Bool**
- 참(True) 과 거짓(False)를 표현하는 자료형
- 0은 False / 0제외 숫자는 다 True
- **Conversion**
- **암시적 형변환** - 파이썬이 자동으로 형변환 하는 것
- 정수와 실수에서 정수가 실수로 바뀜
- 3 + 5.0 = 8.0 
- True + 3 = 4
### 명시적 형변환 - 직접 지정하는 형번환
- str -> int : 형식에 맞는 숫자마 가능
- "3.5" int("3.5")는 불가능 -> float("3.5") 정수는 실수가 될수없음
- ***연산자***
- **복합 연산자**
- 1+=2 , -=, *=, /+, //=, 등
- 비교 연산자
- == , !=, is, is not
- is 메모리 내에서 같은 객체를 참조하는지 확인 (주소값이 같은지 확인)
- 'str'은 주소값이 바뀌지 않지만 list는 주소값이 바뀜
- **논리 연산자**
- and or not
### 단축평가
- (True and True) ('a' and 'b') 이면 'b' 반환
```
vowels = 'aeiou'
print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True
```
- **and 는 False(거짓)이 나오면 중단**
- and 는 True가 나와도 계속 진행
- **or 는 True(참)이 나오면 중단** 
- or 는 False가 나와도 계속 진행
- **멤버쉽 연산자**
- in , not in
0 or 3 or b
## 250729 
- **조건문**
- if, elif, else
- if 표현식:
    -   코드 블록
- if 참(True) 일때 실행
- elif 앞선 조건이 거짓(false)이고 참 일때 실행
- else > 모든 실행이 거짓일때 실행
- **반복문**
- for문 
- 딕셔너리 순회 - 원칙적으로는 순서가 없지만 python3.7부터 삽입(입력)한 순서대로 나옴
```
abc = [1, 2, 3]
for i in range(len(abc)):
    abc[i] = abc[i] * 2

print(abc) # 2, 4, 6
```
- while 문
- 반드시 종료 조건이 있어야함
- while 조건문
- **반복문**
- 반복제어
- break, continue, pass
- break는 반복문을 **즉시 탈출**
- continue 다음 반복으로 건너뜀
- pass 아무런 작업도 하지않고 넘어감
- for else 구문
```
numbers = [1, 3, 5, 6, 7 ,9, 10 ,11]

for number in numbers:
    if number  % 2 == 0:
        print(f'첫번쨰 짝수 {number}찾음')
else:
    print(못찾음)
```
### 함수
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
- 함수 정의는 def 키워드로 시작 (define)
- 함수 이름은 동사 + 명사 로 작성 (make_sum) 컨밴션
- 괄호안에 매개변수를 정의할 수 있다
- **함수 반환 값**
- 함수는 **필요한 경우* 결과를 반환 할수 있음 
- return "반환 값"
- 매개 변수 : 함수를 **정의**할 떄
- 인자 : 함수를 **호출**할 때
- **위치 인자**
- 함수 호출 시 인자으 위치에 따라 전달되는 인자
- 함수에 넣은 인자의 위치에 맞게 들어감
- **기본 인자값**
- 함수 정의단계에서 기본값(default)값을 정해주는것
-  **키워드 인자값**
- 호출시 인자의 이름과 함께 값을 전달하는 인자
- 순서에 상관없이 적용가능
- 호출 시 키워드 인자는 위치 인자 뒤에 위치해야함 (아니면 오류뜸)
- **임의의 인자 목록**
- def adb(*args) <<
- 정해지지 않은 개수의 인자를 처리하는 인자
- list형식이 아닌 tuple 형태로 줌
- 매개변수 앞에 ' * '를 붙여 사용
- **임의의 키워드 인자 목록**
- def adb(**kwargs) 
- 매개변수 앞에 ' ** ' 를 붙여 사용
### python의 범위(soope)
- local scope에 존재하기 떄문에 global scope에서는 사용할수 없음
- local에 지정한 변수는 global에서 사용 불가

- built-in scope
- 파이썬이 실행된 이후부터 영원히 유지되는 것
- scope의 순서 **LEGB Rule**

### **lisat comprehension** (리스트 한줄로 쓰기)
- 나중에 공부 다하고 코드 줄이기 하고싶을떄 사용
- 속도가 빠르다는 장점이 있음

### enumerate(iterable, start=0)
- enumerate 인덱스와 value값을 동시에 가져올때 사용
```
fruits = ['apple', 'banana', 'cherry']

for ind, va in enumerate(fruits, start=3):
    print(ind, va)
```
