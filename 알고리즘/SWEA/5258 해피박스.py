T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    product = [list(map(int, input().split())) for _ in range(M)]

    dp = [0] * (N + 1)

    for size, price in product:
        for j in range(N, size - 1, -1):
            dp[j] = max(dp[j], dp[j - size] + price)

    print(f"#{tc} {dp[N]}")
