#!/usr/bin/python3


"""Calculate fewest coins needed to meet a total"""


def makeChange(coins, total):
    """runs through coins to find lowest amount to get total"""
    if total <= 0:
        return 0

    if coins is None:
        return -1

    sorted_coins = sorted(coins, reverse=True)
    coin_counter = 0
    current_change = total

    while current_change != 0:
        if sorted_coins[0] < total:
            current_change -= sorted_coins[0]
            coin_counter += 1
        for coin in sorted_coins:
            if current_change % coin == 0:
                coin_counter += current_change // coin
                current_change -= coin * current_change / coin
                return coin_counter
            elif coin < current_change:
                current_change -= coin
                coin_counter += 1
        return -1

    return coin_counter

print(makeChange([2, 3], 383601))