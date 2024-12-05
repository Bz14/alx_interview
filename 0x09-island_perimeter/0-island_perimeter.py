#!/usr/bin/python3


def island_perimeter(grid):
    """Calculate the perimeter of the island."""
    if not grid or not grid[0]:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    row_len, col_len = len(grid), len(grid[0])
    ans = 0

    def is_inbound(row, col):
        """Check if the position is within the grid bounds."""
        return 0 <= row < row_len and 0 <= col < col_len

    def DFS(row, col):
        """Perform DFS to calculate perimeter."""
        nonlocal ans
        visited.add((row, col))

        for x, y in directions:
            new_row, new_col = row + x, col + y
            if not is_inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                ans += 1
            elif (new_row, new_col) not in visited:
                DFS(new_row, new_col)

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                DFS(i, j)
                return ans

    return 0
