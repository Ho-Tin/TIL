# 거스름돈
# https://www.acmicpc.net/problem/5585

import sys
sys.stdin = open('input.txt')

# 지불 금액
pay = 1000

# 물건가격
money = int(input())

# 거스름돈 개수가 가장 적게
money_kind = (500, 100, 50, 10, 5, 1)

# 가장 비싼것 부터 없애기


def payment(mon):
    count = 0
    while mon:
        if mon >= 500:
            mon -= 500
            count +=1
        elif mon >= 100:
            mon -= 100
            count += 1
        elif mon >= 50:
            mon -= 50
            count += 1
        elif mon >= 10:
            mon -= 10
            count += 1
        elif mon >= 5:
            mon -= 5
            count += 1
        else:
            mon -= 1
            count += 1
    return count

print(payment(pay - money))