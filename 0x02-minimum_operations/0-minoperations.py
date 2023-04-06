#!/usr/bin/python3
"""calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    i = 2
    if n < 2:
        return 0
    while i < n + 1:
        if n % i == 0:
            return minOperations(n // i) + i
        i = i + 1
