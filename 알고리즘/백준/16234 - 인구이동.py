import sys
from collections import deque

sys.stdin = open("input.txt", "r") # 제출 시에는 주석 처리해주세요
# input = sys.stdin.readline

# N: 땅의 크기, L~R: 인구 차이 조건
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우 4방향 탐색을 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited):
    """
    (x, y)에서 시작하여 국경이 열리는 연합을 찾고 반환하는 함수
    """
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    union = []  # 연합에 속한 나라들의 좌표 리스트
    union.append((x, y))

    population_sum = graph[x][y]  # 연합의 인구 총합

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 지도 범위 내에 있고, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(graph[cx][cy] - graph[nx][ny])

                # 인구 차이가 L 이상 R 이하라면 국경 오픈
                if L <= diff <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    population_sum += graph[nx][ny]

    return union, population_sum


days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False  # 오늘 인구 이동이 발생했는지 체크하는 플래그

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 방문하지 않은 나라에서 BFS 시작
                current_union, p_sum = bfs(i, j, visited)

                # 연합에 속한 나라가 2개 이상이면 인구 이동 처리
                if len(current_union) > 1:
                    moved = True
                    new_population = p_sum // len(current_union)

                    # 연합에 속한 모든 나라의 인구 업데이트
                    for ux, uy in current_union:
                        graph[ux][uy] = new_population

    # 인구 이동이 한 번도 없었다면 반복 종료
    if not moved:
        break

    days += 1

print(days)