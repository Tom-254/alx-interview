#!/usr/bin/python3
"""
Returns the name of the player that won the most
rounds or None if the winner cannot be determined
"""


def sieve(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


def play_game(n, primes):
    """
    Simulate a game where two players take turns choosing a prime number from
    a set of consecutive integers starting from 1 up to and including n. The
    player that cannot make a move loses the game.
    """
    turn = 0
    for prime in primes:
        if prime > n:
            break
        turn += 1
    if turn % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """
    Determine the winner of x rounds of a game where two players take turns
    choosing a prime number from a set of consecutive integers starting from 1
    up to and including n. The player that cannot make a move loses the game.
    """
    max_n = max(nums[:x])
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums[:x]:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
