import itertools
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    weight_cho = list(map(int, input().split()))
    cnt = 0

    def generate_subset(index, left_sum, right_sum):
        global cnt
        if right_sum > left_sum:
            return
        if index == N:
            cnt += 1
            return
        generate_subset(index + 1, left_sum + cho[index], right_sum)    # 왼쪽 추에 추가하기
        generate_subset(index + 1, left_sum, right_sum + cho[index])    # 오른쪽 추에 추가하기


    for cho in itertools.permutations(weight_cho):  # 순열 돌려서 집어넣기
        generate_subset(1, cho[0], 0)   # 무조건 1번추는 왼쪽으로 가야하니깐 인덱스 1부터 시작
    print(f'#{tc} {cnt}')
