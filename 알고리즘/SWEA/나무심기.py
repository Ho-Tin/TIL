
T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 나무 개수
    tree = list(map(int, input().split()))
    tree_max = max(tree)
    cnt = 0

    while sum(tree) != (tree_max * N):
        cnt += 1
        tree_min = 121

        if cnt % 2 == 1:        # 홀수인날
            water = 1
            for i in range(N):
                if tree[i] < tree_max:
                    if tree[i] + water == tree_max:
                        tree[i] = tree[i] + water
                        break
                    else:
                        if tree[i] < tree_min:
                            tree_min = tree[i]
                            stage = i
            else:
                if tree[stage] + 2 != tree_max:
                    tree[stage] = tree[stage] + water
                else:
                    continue

        else:
            water = 2       # 짝수인날
            for i in range(N):
                if tree[i] < tree_max:
                    if tree[i] + water == tree_max:
                        tree[i] = tree[i] + water
                        break
                    else:
                        if tree[i] < tree_min:
                            tree_min = tree[i]
                            stage = i
            else:
                if tree[stage] + 2 > tree_max:
                    continue
                else:
                    tree[stage] = tree[stage] + water


    print(f'#{tc} {cnt}')



# 테스트 케이스 수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 나무 개수
    tree = list(map(int, input().split()))
    
    # 1. 목표 높이 설정
    tree_max = max(tree)
    
    # 2. 필요한 +1, +2 물의 총 개수 계산
    total_ones = 0
    total_twos = 0
    
    for t in tree:
        diff = tree_max - t  # 채워야 할 차이
        if diff > 0:
            total_twos += diff // 2
            total_ones += diff % 2
            
    # 3. 최소 날짜 계산 (시뮬레이션)
    days = 0
    while True:
        days += 1
        
        # 'days'일 동안 사용 가능한 +1, +2의 총량
        available_ones = (days + 1) // 2
        available_twos = days // 2
        
        # +2가 부족한지 확인
        deficit_twos = max(0, total_twos - available_twos)
        
        # 부족한 +2를 채우기 위해 필요한 +1의 수 (1개당 2의 비용)
        ones_needed_for_trade = deficit_twos * 2
        
        # 최종적으로 필요한 +1의 총 개수
        total_ones_required = total_ones + ones_needed_for_trade
        
        # 사용 가능한 +1이 최종 필요 +1보다 많거나 같으면 성공
        if available_ones >= total_ones_required:
            break  # while 루프 탈출
            
    print(f'#{tc} {days}')