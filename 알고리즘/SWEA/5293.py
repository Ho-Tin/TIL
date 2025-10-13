from collections import defaultdict, deque
 
T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = list(map(int, input().split()))
 
    N = A + B + C + D + 1
    result = True
    num_list = deque()
    fail_cnt = 0
    while len(num_list) != N:
        if fail_cnt > N:
            result = False
            break
        if A > 0:
            if not num_list:
                num_list.extend('00')
            else:
                if num_list[0] == '0':
                    num_list.extendleft('0')
                elif num_list[-1] == '0':
                    num_list.extend('0')
            A -= 1
 
        if B > 0 and A == 0:
            if not num_list:
                num_list.extend('01')
                B -= 1
            else:
                if num_list[0] == '1':
                    num_list.extendleft('0')
                    B -= 1
                elif num_list[-1] == '0':
                    num_list.extend('1')
                    B -= 1
 
        if C > 0 and A == 0:
            if not num_list:
                num_list.extend('10')
                C -= 1
            else:
                if num_list[0] == '0':
                    num_list.extendleft('1')
                    C -= 1
                elif num_list[-1] == '1':
                    num_list.extend('0')
                    C -= 1
 
        if D > 0 and A == 0 and B == 0 and C == 0:
            if not num_list:
                num_list.extend('11')
                D -= 1
            else:
                if num_list[0] == '1':
                    num_list.extendleft('1')
                    D -= 1
                elif num_list[-1] == '1':
                    num_list.extend('1')
                    D -= 1
 
        fail_cnt += 1
 
 
    if result:
        print(f"#{tc}", ''.join(num_list))
    else:
        print(f"#{tc} impossible")
