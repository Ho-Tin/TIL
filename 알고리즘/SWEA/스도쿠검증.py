
# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
 



# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 


# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


# [제약 사항]

# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# 다음 줄부터 각 테스트 케이스가 주어진다.

# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# [출력]

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.



T = int(input())
for test_case in range(1, T + 1):
    case = 9
    sudoku = [list(map(int, input().split())) for _ in range(case)]

    result = 1
    wid_result = 1
    length_result = 1
    thr_result = 1


    # 가로 열 확인
    for i in range(9):
        wid = []        # 가로 값 초기화
        wid.append(sudoku[i])       # 가로 1줄 슬라이싱
        wid_set = set(*wid)         # 값이 중복인지 확인 (리스트 안의 리스트 언패킹)
        if len(wid_set) != 9:       # 값이 중복이라면 9 이하 이므로 길이가 9인지 확인
            wid_result = 0
            break

    # 세로 열 확인
    for j in range(9):
        length = []     # 세로 값 초기화
        for i in range(9):
            length.append(sudoku[i][j])
        else:
            length_set = set(length)
            if len(length_set) != 9:
                length_result = 0
                break

    # 3x3 확인
    for i in range(0,9,3):
        for j in range(0,9,3):
            thr = []
            for ik in range(3):
                for jk in range(3):
                    ni = i + ik
                    nj = j + jk
                    thr.append(sudoku[ni][nj])
            else:
                thr_set = set(thr)
                if len(thr_set) != 9:
                    thr_result = 0
                    break
    if wid_result + length_result + thr_result == 3:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
