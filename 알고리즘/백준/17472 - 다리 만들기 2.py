# 다리 만들기 2
# https://www.acmicpc.net/problem/17472

import sys
sys.stdin = open('input.txt')
import heapq

N, M = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]

board_visit = [[False] * M for _ in range(N)]
dxy = (1, 0), (-1, 0), (0, 1), (0, -1)


# 섬 찾기
def island(isx, isy, number):
    for ix, iy in dxy:
        ii = ix + isx
        yy = iy + isy
        if 0 <= ii < N and 0 <= yy < M:
            if board[ii][yy] != 0 and not board_visit[ii][yy]:
                board_visit[ii][yy] = True
                board[ii][yy] = number
                island(ii, yy, number)


# 섬 위치 찾기
count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and not board_visit[i][j]:
            count += 1
            board_visit[i][j] = True
            board[i][j] = count
            island(i, j, count)




# 현재섬(다리의 시작점 x, y, 가로세로방향 x, y, 현재 다리의 카운트)
# 만약 다리가 다른 섬을 만나면 즉시 종료 하고 heap 에 추가 - (현재섬, 이은섬의 숫자, 다리개수)
def find_island(fix, fiy, cur_x, cur_y, cnt_num, island_num):
    global heap
    fix_cur_x = fix + cur_x
    fix_cur_y = fiy + cur_y
    if 0 <= fix_cur_x < N and 0 <= fix_cur_y < M:
        if board[fix_cur_x][fix_cur_y] != 0:
            if cnt_num >= 2:
                heap.append((island_num, board[fix_cur_x][fix_cur_y], cnt_num))

            return
        else:
            find_island(fix_cur_x, fix_cur_y, cur_x, cur_y, cnt_num + 1, island_num)
    # 벽, 경계를 만나면 즉시 종료
    else:
        return


heap = []

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    if board[ni][nj] == 0:
                        find_island(ni, nj, dx, dy, 1, board[i][j])

heap = list(set(heap))
heapq.heapify(heap)
heap.sort(key = lambda a: a[2])

island_count = list(range(count + 1))
def find(x):
    # 자신이 루트이면 자기 자신 반환
    if x == island_count[x]:
        return x

    # 자신이 루트가 아니면 부모를 루트로 만듦
    else:
        island_count[x] = find(island_count[x])
    return island_count[x]


def union(x, y):
    x = find(x)
    y = find(y)

    # 부모를 합쳐 줌
    if y < x:
        island_count[x] = y
    else:
        island_count[y] = x

result = 0
edges = 0
for x, y, z, in heap:
    if find(x) != find(y):
        result += z
        edges += 1
        union(x, y)

if count > 0 and edges == count - 1:
    print(result) 
else:
    print(-1)
