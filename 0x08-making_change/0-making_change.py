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

    max_value = total + 1
    dp = [max_value] * max_value
    dp[0] = 0

    for i in range(1, max_value):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == max_value:
        return -1
    else:
        return dp[total]
