import itertools
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    node = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V + 1)


    def make_set(x):
        p[x] = x


    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]


    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px < py:
            p[py] = px
        else:
            p[px] = py


    result_sum = 0


    def mst_kruskal(edges):
        mst = []

        for i in range(V + 1):
            make_set(i)
        edges.sort(key=lambda x: x[2])

        for edge in edges:
            s, e, w = edge
            if find_set(s) != find_set(e):
                union(s, e)
                mst.append(edge)
        return mst


    for result in mst_kruskal(node):
        result_sum += result[2]

    print(f'#{tc} {result_sum}')