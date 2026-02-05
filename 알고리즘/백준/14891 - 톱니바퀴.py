import sys
# 1. 입력 받기 (빠른 입출력 사용)
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('input.txt')

N = 4
wheel = [deque(map(int, input().strip())) for _ in range(N)]
K = int(input())
move = [list(map(int, input().split())) for _ in range(K)]


wheel_dict = {1: [2],
              2: [2, 6],
              3: [2, 6],
              4: [6]
              }


def move_num(wheel_number, wheel_dir):
    moving[wheel_number - 1] = wheel_dir
    for i in wheel_dict[wheel_number]:

        if i == 2:
            if wheel[wheel_number][6] != wheel[wheel_number - 1][i]:
                if moving[wheel_number] == 0:
                    move_num(wheel_number + 1, wheel_dir * -1)
        else:
            if wheel[wheel_number - 1][i] != wheel[wheel_number - 2][2]:
                if moving[wheel_number - 2] == 0:
                    move_num(wheel_number - 1, wheel_dir * -1)


def wheel_move(number, direction):

    if direction == -1:
        wheel[number].rotate(-1)
    elif direction == 1:
        wheel[number].rotate(1)


# 시계 방향 : 1 , 반시계 : -1
for num, dire in move:
    moving = [0] * N
    move_num(num, dire)
    for idx, wheel_num in enumerate(wheel):
        wheel_move(idx, moving[idx])


result = 0
for idx, wheel_num in enumerate(wheel):
    if wheel_num[0] == 1:
        if idx == 0:
            result += 1
        elif idx == 1:
            result += 2
        elif idx == 2:
            result += 4
        else:
            result += 8

print(result)


