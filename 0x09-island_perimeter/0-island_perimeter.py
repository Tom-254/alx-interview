#!/usr/bin/env python3
"""Island perimeter calculating module.
"""


def island_perimeter(grid):
    """Find the perimeter of an island with no lakes.
    """
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 for each land cell

                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
