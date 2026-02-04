import sys
# 1. 입력 받기 (빠른 입출력 사용)

# input = sys.stdin.readline
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
mountain = [list(map(int, input().split())) for _ in range(N)]

dxy = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
result = 0


def bfs(x, y):
    find_mountain = []
    find_mountain.append((x, y))
    visit[x][y] = True
    is_top = True
    while find_mountain:
        fx, fy = find_mountain.pop()

        # mountain_visit[fx][fy] = True
        for dx, dy in dxy:
            ni = fx + dx
            nj = fy + dy
            if 0 <= ni < N and 0 <= nj < M:
                if mountain[ni][nj] > mountain[x][y]:
                    is_top = False
                elif mountain[ni][nj] == mountain[x][y] and not visit[ni][nj]:
                    visit[ni][nj] = True
                    find_mountain.append((ni, nj))

    return 1 if is_top else 0


visit = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visit[i][j] and mountain[i][j] > 0:
            result += bfs(i, j)

print(result)