# https://www.acmicpc.net/problem/14501\
# 퇴사

N = int(input())
diary = [list(map(int, input().split())) for i in range(N)]
# diary(소요일정, 비용)

total_pay = 0


def payment(day_index, pre_pay):
    global total_pay
    if day_index == N:
        if pre_pay > total_pay:
            total_pay = pre_pay
        return
    if day_index > N:
        return
    payment(day_index + 1, pre_pay)

    time = diary[day_index][0]
    pay = diary[day_index][1]

    if day_index + time <= N:
        # 날짜는 (오늘 + 걸리는 시간)으로 점프, 돈은 (현재 돈 + 비용)으로 증가
        payment(day_index + time, pre_pay + pay)


payment(0, 0)

print(total_pay)