# 알고리즘/자료구조/정렬/수학적 개념

## 1. 알고리즘의 정의와 5대 특성
- 알고리즘: 문제를 해결하기 위한 절차적 방법, 명확한 입력/출력, 유한성, 효과성, 명확성
- 5대 특성: 정확성, 작업량(효율성), 메모리 사용량, 단순성, 최적성
- 좋은 알고리즘: 정확하고, 빠르고, 메모리 적게 사용, 단순하며, 더 이상 개선 불가

## 2. 시간복잡도/공간복잡도(Big-O)
- 시간복잡도: 입력 크기 N에 따른 연산 횟수 증가율, O(1), O(N), O(N^2), O(logN) 등
- 공간복잡도: 입력 크기 N에 따른 메모리 사용량 증가율
- Big-O 표기법: 최고차항만 남기고 계수/상수는 생략
- 예시: for문 1번 = O(N), 중첩 for문 = O(N^2)

## 3. 자료구조 활용
- 1차원/2차원 리스트, 행/열 우선 순회, 델타 탐색(dx, dy)
- 예시:
```python
arr = [[1,2],[3,4]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j])
```
- 델타 탐색:
```python
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for x in range(N):
    for y in range(M):
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
```

## 4. 예외처리 및 파일입출력
- try-except, else, finally, as 키워드
- pathlib: 파일/폴더 경로 관리, exists(), is_file() 등
- json: dumps, loads, dump, load 등
- 예시:
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print('0으로 나눌 수 없음:', e)
finally:
    print('항상 실행')
```

## 5. 실전 팁
- git 명령어: init, add, commit, push, pull, clone, log 등
- VSCode 사용법: 폴더 열기(code .), 터미널, 확장 프로그램 등
- API 활용: requests, json 등
- 디버깅: print, breakpoint, IDE 디버거
- 공식 문서, 시각화 도구 적극 활용
