#!/usr/bin/python3
"""Determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
to meet a given amount total.
"""
    if total <= 0:
        return 0

    max_value = float('inf')
    dp = [max_value] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != max_value else -1
