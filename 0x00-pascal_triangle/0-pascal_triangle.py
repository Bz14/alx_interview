#!/usr/bin/python3
"""A module for Pascal's Triangle."""


def pascal_triangle(n):
    """ Function to print pascal triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
