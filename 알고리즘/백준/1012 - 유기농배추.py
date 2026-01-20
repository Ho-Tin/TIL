# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
from pprint import pprint
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    M, N, K = list(map(int, input().split()))
    baechu = [list(map(int, input().split())) for _ in range(K)]
    baechu_map = [[0] * M for _ in range(N)]

    dxy = (0, 1), (0, -1), (-1, 0), (1, 0)
    for a, b in baechu:
        baechu_map[b][a] = 1

    queue = deque()

    def dfs(cx, cy):
        queue.append((cx, cy))
        visit[cx][cy] = True
        while queue:
            x, y = queue.popleft()

            for dx, dy in dxy:
                ni = dx + x
                nj = dy + y
                if 0 <= ni < N and 0 <= nj < M:
                    if baechu_map[ni][nj] and not visit[ni][nj]:
                        queue.append((ni, nj))
                        visit[ni][nj] = True
        return visit

    count = 0
    visit = [[False] * M for _ in range(N)]

    for ccy, ccx in baechu:
        if not visit[ccx][ccy]:
            dfs(ccx, ccy)
            count += 1

    print(count)