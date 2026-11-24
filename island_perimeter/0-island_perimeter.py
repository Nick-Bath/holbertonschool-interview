#!/usr/bin/python3

"""Calculate perimeter of an island"""

def island_perimeter(grid):
    """loop through grid to find land"""
    perimeter = 0
    i = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col != 1:
                continue
            if col == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == len(row) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
