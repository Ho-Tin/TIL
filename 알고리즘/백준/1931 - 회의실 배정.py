# 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys
sys.stdin = open('input.txt')

# 회의수
# input = sys.stdin.readline
N = int(input())


meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
start = 0
end = 0

for st, en in meeting:
    if end <= st:
        end = en
        count += 1

print(count)