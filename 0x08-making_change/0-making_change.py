#!/usr/bin/python3
""" Coin change"""


def makeChange(coins, total):
    n = len(coins)
    memo = {}

    def dp(amount):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        minVal = float('inf')
        for i in range(n):
            if coins[i] <= amount:
                minVal = min(minVal, 1 + dp(amount - coins[i]))
        memo[amount] = minVal
        return memo[amount]
    ans = dp(total)
    return -1 if ans == float('inf') else ans
