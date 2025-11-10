# 정렬 알고리즘

## 1. 버블정렬(Bubble Sort)
- 인접한 두 원소를 비교해가며 큰 값을 뒤로 보내는 방식
- 시간복잡도: O(N^2), 공간복잡도: O(1)
- 특징: 구현이 매우 쉽지만 비효율적, 거의 사용하지 않음
- 예시:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
- 실전 팁: 데이터가 거의 정렬되어 있을 때만 고려

## 2. 선택정렬(Selection Sort)
- 남은 데이터 중 최솟값을 찾아 맨 앞과 교환
- 시간복잡도: O(N^2), 공간복잡도: O(1)
- 특징: 교환 횟수가 적음, 구현이 쉬움
- 예시:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

## 3. 삽입정렬(Insertion Sort)
- 이미 정렬된 부분에 새 원소를 알맞은 위치에 삽입
- 시간복잡도: O(N^2), 공간복잡도: O(1)
- 특징: 거의 정렬된 데이터에 매우 빠름
- 예시:
```python
def insertion_sort(arr):
    n = len(arr)
    for idx in range(1, n):
        for jdx in range(idx, 0, -1):
            if arr[jdx-1] > arr[jdx]:
                arr[jdx-1], arr[jdx] = arr[jdx], arr[jdx-1]
            else:
                break
    return arr
```

## 4. 카운팅정렬(Counting Sort)
- 각 값의 발생 횟수를 세어 정렬, 정수 데이터에만 사용
- 시간복잡도: O(N+K), 공간복잡도: O(N+K)
- 특징: 데이터 범위가 작을 때 매우 빠름, 비교 연산 없음
- 예시:
```python
def counting_sort(arr, max_value):
    n = len(arr)
    count_arr = [0] * (max_value + 1)
    result = [0] * n
    for num in arr:
        count_arr[num] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    for i in range(n-1, -1, -1):
        val = arr[i]
        result[count_arr[val] - 1] = val
        count_arr[val] -= 1
    return result
```

## 5. 기타 정렬
- 병합정렬, 퀵정렬, 힙정렬 등 고급 정렬은 표준 라이브러리(sorted, sort)에서 사용
- 실전에서는 내장 정렬 함수 사용 권장

## 6. 정렬 알고리즘 비교
| 알고리즘 | 시간복잡도 | 공간복잡도 | 특징 |
|---|---|---|---|
| 버블정렬 | O(N^2) | O(1) | 구현 쉬움, 비효율적 |
| 선택정렬 | O(N^2) | O(1) | 교환 적음, 비효율적 |
| 삽입정렬 | O(N^2) | O(1) | 거의 정렬된 데이터에 빠름 |
| 카운팅정렬 | O(N+K) | O(N+K) | 정수 데이터, 범위 작을 때 빠름 |
| 병합/퀵/힙 | O(NlogN) | O(N)~O(1) | 실전에서 주로 사용 |
