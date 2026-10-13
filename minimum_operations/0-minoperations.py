#!/usr/bin/python3
"""Module: Find the minimum operations"""

def minOperations(n):
    """Minimum operations via recursion"""
    ops = 0

    for factor in range(2, n + 1):
        if factor == n:
            return n
        if n % factor != 0:
            continue
        if n % factor == 0:
            ops += factor + minOperations(int(n / factor))
            break
    return ops





