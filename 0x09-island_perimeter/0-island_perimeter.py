#!/usr/bin/python3
"""Island Perimeter using BFS"""


def island_perimeter(grid):
    """Calculate the perimeter of the island using BFS."""
    if not grid or not grid[0]:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    row_len, col_len = len(grid), len(grid[0])
    visited = set()

    def is_inbound(row, col):
        """Check if the position is within the grid bounds."""
        return 0 <= row < row_len and 0 <= col < col_len

    def BFS(start_row, start_col):
        """Perform BFS to calculate the perimeter."""
        queue = [(start_row, start_col)]
        visited.add((start_row, start_col))
        perimeter = 0

        while queue:
            row, col = queue.pop(0)
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if (not is_inbound(new_row, new_col) or grid[new_row][new_col] == 0):
                    perimeter += 1
                elif ((new_row, new_col) not in visited
                      and grid[new_row][new_col] == 1):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
        return perimeter

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                return BFS(i, j)

    return 0
