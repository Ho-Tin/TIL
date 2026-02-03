import sys
from itertools import permutations

# 1. 입력 받기 (빠른 입출력 사용)
input = sys.stdin.readline
N = int(input())
# 각 이닝별 선수들의 결과를 저장 (N행 9열)
innings = [list(map(int, input().split())) for _ in range(N)]


# 2. 타순 정하기 및 시뮬레이션
max_score = 0
for idx in permutations(range(1, 9), 8):
    order = list(idx[:3]) + [0] + list(idx[3:])

    score = 0   # 현재 점수
    idx = 0     # 현재 타순
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            player = order[idx]
            result = inning[player]
            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif result == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif result == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            else:
                score += b3 + b2 + b1 + 1
                b3, b2, b1 = 0, 0, 0

            idx = (idx + 1) % 9

    max_score = max(score, max_score)
print(max_score)