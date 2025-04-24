t = int(input())
for _ in range(t):
    price = int(input())
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    max_coin = max(coins)
    max_val = price + max_coin
    INF = float("inf")
    dp = [INF] * (max_val + 1)
    dp[0] = 0

    for coin in coins:
        for v in range(max_val, coin - 1, -1):
            dp[v] = min(dp[v], dp[v - coin] + 1)

    for paid in range(price, max_val + 1):
        if dp[paid] != INF:
            print(f"{paid} {dp[paid]}")
            break
