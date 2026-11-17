#!/usr/bin/python3


"""Calculate fewest coins needed to meet a total"""


def makeChange(coins, total):
    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                min_coins[i] = min(min_coins[i], 1 + min_coins[i-c])
            
    return min_coins[-1] if min_coins[-1] != total + 1 else -1 