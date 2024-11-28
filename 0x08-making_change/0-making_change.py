#!/usr/bin/python3
""" Coin change"""


def makeChange(coins, total):
    dp = [float('inf') for _ in range(total + 1)]
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[total] == float('inf') else dp[total]
