#!/usr/bin/node

def island_perimeter(grid):

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
