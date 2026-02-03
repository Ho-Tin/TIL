import sys
from itertools import permutations
# 1. 입력 받기 (빠른 입출력 사용)
# input = sys.stdin.readline
sys.stdin = open('input.txt')
N, M = list(map(int, input().split()))
# 각 이닝별 선수들의 결과를 저장 (N행 9열)
square = [list(map(int, input().strip())) for _ in range(N)]

min_num = min(N, M)
max_sum = min(N, M) ** 2
dxy = (0, 1), (1, 1), (1, 0)

max_result = 1     # 1x1 정사각형
for i in range(N):
    for j in range(M):
        if max_sum == max_result:
            break
        for k in range(1, min_num):
            cnt = 0
            for dx, dy in dxy:
                ni = i + dx * k
                nj = j + dy * k
                if 0 <= ni < N and 0 <= nj < M:
                    if square[ni][nj] == square[i][j]:
                        cnt += 1
            if cnt == 3:
                result = (k + 1) ** 2
                max_result = max(max_result, result)


print(max_result)
