#!/usr/bin/python3

"""Calculate perimeter of an island"""

def island_perimeter(grid):
    """loop through grid to find land"""
    perimeter = 0
    i = 0

    for row in grid:
        j = 0
        for col in row:
            if col == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
            j += 1
        i += 1

    return perimeter
