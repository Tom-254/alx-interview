#!/usr/bin/python3
"""Determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    memo = {}

    def change(amount):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        min_coins = float('inf')
        for coin in coins:
            remaining_coins = change(amount - coin)
            min_coins = min(min_coins, remaining_coins + 1)

        memo[amount] = min_coins
        return min_coins

    result = change(total)

    if result == float('inf'):
        return -1
    else:
        return result
