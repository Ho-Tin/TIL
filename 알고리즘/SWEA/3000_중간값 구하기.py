import heapq
 
T = int(input())
for tc in range(1, T + 1):
    N, A = list(map(int, input().split()))
    number = [list(map(int, input().split())) for _ in range(N)]
 
    min_heap = []
    max_heap = []
    mod = 20171109
    center_num = A
    heapq.heappush(max_heap, A)
    result_sum = 0
    min_sum = 0
    max_sum = 1
    result = 0
    for node in number:
        node.sort()
        for i in node:
            if node[1] < center_num or node[0] > center_num:
                if i >= center_num:
                    heapq.heappush(max_heap, i)
                    max_sum += 1
                    if abs(max_sum - min_sum) > 1:
                        heapq.heappush(min_heap, -heapq.heappop(max_heap))
                        max_sum -= 1
                        min_sum += 1
                else:
                    heapq.heappush(min_heap, -i)
                    min_sum += 1
                    if abs(max_sum - min_sum) > 1:
                        heapq.heappush(max_heap, -heapq.heappop(min_heap))
                        min_sum -= 1
                        max_sum += 1
 
            else:
                if i >= center_num:
                    heapq.heappush(max_heap, i)
                    max_sum += 1
                else:
                    heapq.heappush(min_heap, -i)
                    min_sum += 1
 
        else:
            if min_sum > max_sum:
                center_num = -heapq.heappop(min_heap)
                heapq.heappush(min_heap, -center_num)
 
            else:
                center_num = heapq.heappop(max_heap)
                heapq.heappush(max_heap, center_num)
 
        result += center_num
 
    result_sum = result % mod
 
    print(f'#{tc} {result_sum}')
