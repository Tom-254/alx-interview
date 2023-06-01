#!/usr/bin/python3
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


def play_game(n):
    """
    Simulate a game where two players take turns choosing a prime number from
    a set of consecutive integers starting from 1 up to and including n. The
    player that cannot make a move loses the game.
    """
    primes = sieve(n)
    turn = 0
    while primes:
        prime = primes.pop(0)
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
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
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
