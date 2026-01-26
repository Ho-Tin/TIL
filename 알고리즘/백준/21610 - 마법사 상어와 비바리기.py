# 마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610

N, M = list(map(int, input().split()))
# 현재 맵
bag = [list(map(int, input().split())) for _ in range(N)]

# 방향, 이동
move = [list(map(int, input().split())) for _ in range(M)]

# storm 첫 시작
storm_move = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

# 방향 : 재자리, ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dxy = (0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)
water_bug = (-1, -1), (-1, 1), (1, -1), (1, 1)
board = [[0] * N for _ in range(N)]



# 물복사버그
def water(wwx, wwy):
    count = 0
    for a, b in water_bug:
        ni = a + wwx
        nj = b + wwy
        if 0 <= ni < N and 0 <= nj < N:
            if bag[ni][nj] >= 1:
                count += 1
    bag[wwx][wwy] += count


for di, mi in move:
    # 구름 이동
    storm = []
    while storm_move:
        x, y = storm_move.pop()
        mx = ((dxy[di][0] * mi) + x) % N
        my = ((dxy[di][1] * mi) + y) % N
        # 이동완료후 구름이 생김
        board[mx][my] = 1
        storm.append((mx, my))

    # 구름 이동후 1씩 증가
    storm_move = storm
    for sx, sy in storm_move:
        bag[sx][sy] += 1

    # 물복사버그
    for wx, wy in storm_move:
        water(wx, wy)

    # 물복사 버그 끝난후 구름 초기화
    storm_move = []

    # 구름 생성하기
    for i in range(N):
        for j in range(N):
            if bag[i][j] >= 2:
                if board[i][j] != 1:
                    bag[i][j] -= 2
                    storm_move.append((i, j))
                else:
                    board[i][j] = 0

result = 0

for i in range(N):
    for j in range(N):
        result += bag[i][j]

print(result)