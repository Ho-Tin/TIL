# https://www.acmicpc.net/problem/14503
# 로봇 청소기



# 숫자 개수
N, M = list(map(int, input().split()))
# ( 현재 로봇 좌표,x,y),
# d(0, 1, 2, 3 :
#   북, 동, 남, 서)
moving = list(map(int, input().split()))
# N : row 크기, M : column 크기
# 0 : 청소되지 않은 빈칸
# 1 : 벽이 있음
room = [list(map(int, input().split())) for _ in range(N)]
# 북, 동, 남, 서
dxy = (-1, 0), (0, 1), (1, 0), (0, -1)

while True:
    count = 0
    room[moving[0]][moving[1]] = 2
    # 4방향중 0 있을때(청소할곳)
    for dx, dy in dxy:
        ni = dx + moving[0]
        nj = dy + moving[1]
        if room[ni][nj] == 0:
            count += 1
            break
    # count가 변하면 청소할곳이 있다는 소리
    if count > 0:
        moving[2] = (moving[2] + 3) % 4
        move_x = dxy[moving[2]][0] + moving[0]
        move_y = dxy[moving[2]][1] + moving[1]
        if room[move_x][move_y] == 0:
            moving[0], moving[1] = move_x, move_y

    # 4방향중 0 없으면(벽이거나, 이미 청소했거나)
    else:
        move_x = dxy[(moving[2] + 2) % 4][0] + moving[0]
        move_y = dxy[(moving[2] + 2) % 4][1] + moving[1]
        if room[move_x][move_y] == 1:
            break
        else:
            moving[0], moving[1] = move_x, move_y


total_count = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == 2:
            total_count += 1

print(total_count)
