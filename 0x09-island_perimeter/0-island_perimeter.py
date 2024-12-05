#!/usr/bin/python3
""" Island perimeter"""


def island_perimeter(grid):
    """island perimeter"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    ans = 0
    row_len = len(grid)
    col_len = len(grid[0])

    def is_inbound(row, col):
        """is inbound"""
        return (row >= 0 and row < row_len) and (col >= 0 and col < col_len)

    def DFS(row, col):
        """DFS"""
        nonlocal ans
        if not is_inbound(row, col) or grid[row][col] == 0:
            ans += 1
            return
        visited.add((row, col))
        for x, y in directions:
            new_row = row + x
            new_col = col + y
            if (new_row, new_col) not in visited:
                DFS(new_row, new_col)

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                DFS(i, j)
                return ans
