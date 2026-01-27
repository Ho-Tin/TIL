# 연구소
# https://www.acmicpc.net/problem/14502
from itertools import combinations
import sys
from copy import deepcopy

from pprint import pprint
# sys.stdin = open('input.txt')

# 회의수
# input = sys.stdin.readline
N, M = list(map(int, input().split()))
# 빈칸, 벽, 바이러스 / 0, 1, / 벽 3개를 새워야함
board = [list(map(int, input().split())) for _ in range(N)]

result = float('-inf')
# 벽을 새울수 있는 위치
dxy = (0, 1), (0, -1), (1, 0), (-1, 0)


# 바이러스 증식
def virus(virus_x, virus_y, visit, board_co):
    for dx, dy in dxy:
        ni = virus_x + dx
        nj = virus_y + dy
        if 0 <= ni < N and 0 <= nj < M:
            if board_co[ni][nj] == 0:
                visit[ni][nj] = True
                board_co[ni][nj] = 2
                virus(ni, nj, visit, board_co)


wall = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            wall.append((i, j))


for x, y, z in combinations(wall, 3):
    visited = [[False] * M for _ in range(N)]
    board_copy = deepcopy(board)
    board_copy[x[0]][x[1]] = 1
    board_copy[y[0]][y[1]] = 1
    board_copy[z[0]][z[1]] = 1
    count = 0

    for i in range(N):
        for j in range(M):
            if board_copy[i][j] == 2:
                visited[i][j] = True
                virus(i, j, visited, board_copy)

    for i in range(N):
        for j in range(M):
            if board_copy[i][j] == 0:
                count += 1
    result = max(result, count)


print(result)
