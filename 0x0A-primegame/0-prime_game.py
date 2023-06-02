#!/usr/bin/python3
"""
Returns the name of the player that won the most
rounds or None if the winner cannot be determined
"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of a game where two players take turns
    choosing a prime number from a set of consecutive integers starting from 1
    up to and including n. The player that cannot make a move loses the game.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = sum(primes[0: n])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
