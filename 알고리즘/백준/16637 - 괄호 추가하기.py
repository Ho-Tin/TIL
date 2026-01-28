# 괄호 추가하기
# https://www.acmicpc.net/problem/16637

import sys
sys.stdin = open('input.txt')


N = int(input())

word = list(map(str, input().strip()))


def calculation(num_one, num_two, symbol):
    if symbol == '+':
        return num_one + num_two
    elif symbol == '-':
        return num_one - num_two
    else:
        return num_one * num_two


max_result = float('-inf')


def dfs(idx, current_num):
    global max_result
    # idx 가 N(끝)이면 종료
    if idx + 1 == N:
        max_result = max(max_result, current_num)
        return
    next_num = int(word[idx + 2])
    next_sym = word[idx + 1]

    dfs(idx + 2, calculation(current_num, next_num, next_sym))
    # 그 다음 숫자(괄호) 부터 계산
    if (idx + 4) < N:
        bracket_num_one = int(word[idx + 2])
        bracket_num_two = int(word[idx + 4])
        bracket_sym = word[idx + 3]
        bracket_num = calculation(bracket_num_one, bracket_num_two, bracket_sym)
        dfs(idx + 4, calculation(current_num, bracket_num, next_sym))


dfs(0, int(word[0]))

print(max_result)