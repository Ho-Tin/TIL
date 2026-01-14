# https://www.acmicpc.net/problem/14888
# 연산끼워넣기

N = int(input())
# 숫자
number = list(map(int, input().split()))
# 덧셈, 뺼셈, 곱셈, 나눗셈
symbol = list(map(int, input().split()))
max_num = float('-inf')
min_num = float('inf')


def symbol_count(plu, miu, mul, div, idx, total_num):
    global max_num, min_num
    if plu < 0 or miu < 0 or mul < 0 or div < 0:
        return
    if plu + miu + mul + div == 0:
        max_num = max(max_num, total_num)
        min_num = min(min_num, total_num)
        return

    next_num = number[idx]

    symbol_count(plu - 1, miu, mul, div, idx + 1, total_num + next_num)
    symbol_count(plu, miu - 1, mul, div, idx + 1, total_num - next_num)
    symbol_count(plu, miu, mul - 1, div, idx + 1, total_num * next_num)
    symbol_count(plu, miu, mul, div - 1, idx + 1, int(total_num / next_num))


symbol_count(*symbol, 1, number[0])

print(max_num)
print(min_num)