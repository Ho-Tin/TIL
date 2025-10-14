import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    node = list(map(int, input().split()))
    number = []


    def find_par(idx, sum_node, num):
        global result_sum
        idx = idx // 2
        if idx > 0:
            sum_node += num[idx - 1]
            find_par(idx, sum_node, num)
        else:
            result_sum = sum_node
            return


    for i in node:
        heapq.heappush(number, i)

    result_sum = 0
    find_par(N, 0, number)
    print(f'#{tc} {result_sum}')