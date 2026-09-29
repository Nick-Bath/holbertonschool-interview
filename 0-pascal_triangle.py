#!/usr/bin/python3
"""Module: Pascals Triangle."""


def pascal_triangle(n):
    """returns a list of lists containing pascal's triangle"""
    list = []
    if n <= 0:
        return list
    for i in range(n):
        list2 = []
        for j in range(i + 1):
            if j == 0 or j == i:
                list2.append(1)
            else:
                sum = list[i - 1][j] + list[i - 1][j - 1]
                list2.append(sum)
        list.append(list2)
    return list
