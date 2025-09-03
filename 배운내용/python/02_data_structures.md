# 자료구조 이론 및 실전

## 1. 선형구조
### 리스트(List)
- 순서O, 변경O, 중복O, 다양한 타입 저장 가능
- 주요 메서드: append, extend, insert, remove, pop, clear, index, count, reverse, sort
- 슬라이싱, 리스트 컴프리헨션, 얕은/깊은 복사
- 예시:
```python
lst = [1,2,3]
lst.append(4)
lst2 = lst[:]
```

### 스택(Stack)
- LIFO(Last-In-First-Out), 마지막에 들어온 데이터가 먼저 나감
- 주요 연산: push(삽입), pop(삭제), peek/top(맨 위 확인), isEmpty
- 파이썬에서는 리스트로 구현, collections.deque도 사용 가능
- 예시:
```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop()) # 2
```
- 실전 팁: 함수 호출 스택, 웹 브라우저 뒤로가기 등에서 활용

### 큐(Queue)
- FIFO(First-In-First-Out), 먼저 들어온 데이터가 먼저 나감
- 주요 연산: enqueue(삽입), dequeue(삭제), isEmpty
- 파이썬에서는 collections.deque로 구현 권장
- 예시:
```python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft()) # 1
```
- 실전 팁: BFS, 프린터 대기열 등에서 활용

### 연결리스트(Linked List)
- 각 노드가 데이터와 다음 노드의 참조(링크)를 가짐
- 삽입/삭제가 빠름, 크기 제한 없음, 순차 접근만 가능
- 예시:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
```
- 실전 팁: 파이썬 기본 자료구조에는 없음, 직접 구현 필요

## 2. 비선형구조
### 트리(Tree)
- 계층적 구조, 부모-자식 관계, 루트/리프/서브트리 개념
- 이진트리, 이진탐색트리, 힙, 트라이 등 다양한 응용
- 예시(간단):
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

### 그래프(Graph)
- 정점(Vertex)과 간선(Edge)으로 구성, 방향/무방향, 가중치 등
- 인접리스트/인접행렬로 구현
- 예시(인접리스트):
```python
graph = {1: [2,3], 2: [1,4], 3: [1], 4: [2]}
```

## 3. 얕은/깊은 복사
- 리스트 슬라이싱, copy(), copy.deepcopy() 차이 설명
- 얕은 복사: 한 단계만 복사, 내부 객체는 공유
- 깊은 복사: 내부 객체까지 모두 새로 복사
- 예시:
```python
import copy
lst1 = [[1,2],[3,4]]
lst2 = lst1[:]
lst3 = copy.deepcopy(lst1)
```

## 4. 실전 팁
- 자료구조 선택은 시간/공간 복잡도, 사용 목적에 따라 결정
- collections, heapq, queue 등 표준 라이브러리 적극 활용
