import sys
from itertools import permutations

# 1. 입력 받기 (빠른 입출력 사용)
input = sys.stdin.readline
N = int(input())
# 각 이닝별 선수들의 결과를 저장 (N행 9열)
innings = [list(map(int, input().split())) for _ in range(N)]


# 2. 타순 정하기 및 시뮬레이션
def solve():
    max_score = 0

    # 0번 선수(1번 타자)를 제외한 1~8번 선수들의 순서를 정함 (8!)
    for p in permutations(range(1, 9), 8):
        # 4번 타자(인덱스 3) 자리에 0번 선수를 넣음
        # p[:3] (1~3번 타자) + [0] (4번 타자) + p[3:] (5~9번 타자)
        order = list(p[:3]) + [0] + list(p[3:])

        score = 0
        idx = 0  # 현재 타석에 설 타자의 순서 (0~8) - 이닝이 바뀌어도 유지됨!

        # N번의 이닝 진행
        for inning in innings:
            out = 0
            b1, b2, b3 = 0, 0, 0  # 1루, 2루, 3루 주자 상태 (0:없음, 1:있음)

            while out < 3:
                player = order[idx]  # 현재 타석에 선 선수 번호
                result = inning[player]  # 그 선수의 이번 이닝 결과

                if result == 0:  # 아웃
                    out += 1
                elif result == 1:  # 안타
                    score += b3
                    b3, b2, b1 = b2, b1, 1
                elif result == 2:  # 2루타
                    score += b3 + b2
                    b3, b2, b1 = b1, 1, 0
                elif result == 3:  # 3루타
                    score += b3 + b2 + b1
                    b3, b2, b1 = 1, 0, 0
                elif result == 4:  # 홈런
                    score += b3 + b2 + b1 + 1
                    b3, b2, b1 = 0, 0, 0

                # 다음 타자로 넘어감 (9명이므로 9로 나눈 나머지)
                idx = (idx + 1) % 9

        # 최대 점수 갱신
        max_score = max(max_score, score)

    print(max_score)


if __name__ == "__main__":
    solve()