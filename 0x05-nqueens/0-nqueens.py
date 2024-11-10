#!/usr/bin/python3
""" N queens problem """
import sys


def isSafe(board, row, col, n):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col, n):
    """ Solve N queens problem """
    if col == n:
        res = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    res.append([i, j])
        print(res)
        return
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def solveNQueen(n):
    """ Solve N queens problem """
    board = [[0 for j in range(n)] for i in range(n)]
    solve(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQueen(n)
    sys.exit(0)
