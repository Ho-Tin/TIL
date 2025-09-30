T = int(input())
 
for tc in range(1, T + 1):
    N, M, time = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
 
    cells = {}
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not grid[i][j]:
                cells[(i, j)] = [grid[i][j], 0, grid[i][j]]
            else:
                cells[(i, j)] = [grid[i][j], 2, grid[i][j]]
    # [0] = 생명력,[1]= 현재 상태, [2] = 세포 시간
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 줄기 세포 배양
 
    while cnt != time:
 
        cell_dict = {}
        for ke, va in cells.items():
            # 활성화 상태에서 1시간이 지났을때
            if va[1] == 1 and va[0] == va[2]:
                for dx, dy in dxy:
                    ni = ke[0] + dx
                    nj = ke[1] + dy
                    if (ni, nj) not in cells:
                        if (ni, nj) in cell_dict:
                            if cell_dict[(ni, nj)][0] < va[0]:
                                cell_dict[(ni, nj)] = [va[0], 2, va[0]]
                        else:
                            cell_dict[(ni, nj)] = [va[0], 2, va[0]]
                    elif cells[(ni, nj)][0] == 0:
                        if (ni, nj) in cell_dict:
                            if cell_dict[(ni, nj)][0] < va[0]:
                                cell_dict[(ni, nj)] = [va[0], 2, va[0]]
                        else:
                            cell_dict[(ni, nj)] = [va[0], 2, va[0]]
            if va[2] > 0:
                va[2] -= 1
                if va[2] == 0:
                    if va[1] > 0:
                        va[1] -= 1
                        va[2] = va[0]
        # 세포 활동 종료 후 배양할 세포들 추가
        if cell_dict:
            for ke, va in cell_dict.items():
                cells[ke] = va
 
        cnt += 1
    count = 0
    for ke, va in cells.items():
        if va[1] > 0:
            count += 1
    print(f'#{tc} {count}')
