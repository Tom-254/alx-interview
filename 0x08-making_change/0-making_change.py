#!/usr/bin/python3
"""Determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
    to meet a given amount total.
    Greedy Approach which is not always the optimal
    solution
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count
