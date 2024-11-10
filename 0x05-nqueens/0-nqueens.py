#!/usr/bin/python3
""" Solution to the NQueens problem """
import sys


def backtrack(r, n, cols, pos, neg, board):
    """ backtrack function to find solution """
    if r == n:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    res.append([i, j])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def NQueens(n):
    """ Solution to NQueens problem """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(n[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)
        NQueens(num)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
