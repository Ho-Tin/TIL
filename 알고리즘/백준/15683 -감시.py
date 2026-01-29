# 감시
# https://www.acmicpc.net/problem/15683

import sys
sys.stdin = open('input.txt')
from copy import deepcopy

N, M = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(N)]
dxy = (0, 1), (-1, 0), (0, -1), (1, 0)

cctv_shapes = {
    1: [0],            # 한쪽
    2: [0, 2],         # 양옆 (우, 좌)
    3: [0, 1],         # 직각 (우, 상)
    4: [0, 1, 2],      # 세 방향 (우, 좌, 상)
    5: [0, 1, 2, 3],    # 네 방향
}
cnt = 0
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cnt += 1
            cctv.append([i, j, room[i][j], 0])  # x, y, cctv 번호, 회전방향

count = [0] * cnt

max_num = max(N, M)

# cctv가 보는방향 #으로 표시
def cctv_find(cx, cy, cctv_num, room_dcopy, cctv_turn):
    for cctv_idx in cctv_shapes[cctv_num]:
        for ci in range(1, max_num):
            dx, dy = dxy[(cctv_idx + cctv_turn) % 4]
            ni = cx + dx * ci
            nj = cy + dy * ci
            if 0 <= ni < N and 0 <= nj < M:
                if room_dcopy[ni][nj] == 6:
                    break
                else:
                    room_dcopy[ni][nj] = '#'


turn_cnt = 0
min_result = float('inf')
while True:
    result = 0
    room_copy = deepcopy(room)
    for x, y, num, turn in cctv:
        cctv_find(x, y, num, room_copy, turn)
    for i in range(N):
        for j in range(M):
            if room_copy[i][j] == 0:
                result += 1
    min_result = min(min_result, result)

    idx = cnt - 1
    while idx >= 0:
        cctv[idx][3] += 1
        if cctv[idx][3] < 4:  # 0, 1, 2, 3까지는 정상 범위
            break
        else:
            cctv[idx][3] = 0  # 4가 되면 0으로 만들고 앞자리 올림
            idx -= 1

    # 4. 모든 CCTV의 조합을 다 돌았다면(모든 자릿수에서 올림 발생) 종료
    if idx == -1:
        break

print(min_result)