# https://www.acmicpc.net/problem/20055
import sys
# 1. 입력 받기 (빠른 입출력 사용)
from collections import deque
input = sys.stdin.readline
# sys.stdin = open('input.txt')

N, K = list(map(int, input().split()))
belt = deque(list(map(int, input().split())))


robot_tf = deque([False] * N)
result = 0
cnt = 0

while True:
    result += 1
    # 1. 컨베이터 벨트 회전
    belt.rotate(1)
    robot_tf.rotate(1)
    robot_tf[N - 1] = False

    # 2. 첫 로봇부터 스스로 이동
    for i in range(N-2, -1, -1):
        if robot_tf[i] and not robot_tf[i + 1] and belt[i + 1] > 0:
            robot_tf[i + 1] = True
            robot_tf[i] = False
            belt[i + 1] -= 1

            if belt[i + 1] == 0:
                cnt += 1

            # 아니면 그냥 진행
    robot_tf[N - 1] = False

    # 3. 로봇 올리기
    if belt[0] > 0:
        robot_tf[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    if cnt >= K:
        break


print(result)