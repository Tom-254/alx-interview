#!/usr/bin/python3
"""minop"""


def minOperations(n):
    """ min ops"""
    i = 2
    if n < 2:
        return 0
    while i < n + 1:
        if n % i == 0:
            return minOperations(n // i) + i
        i = i + 1
        