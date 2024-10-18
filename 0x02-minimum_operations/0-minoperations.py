#!/usr/bin/python3
""" Minimum operations """


def minOperations(n):
    """ Minimum operation """
    op = 0
    st = "H"
    char = 'H'

    while len(st) < n:
        if n % len(st) == 0:
            op += 2
            char = st
            st += st
        else:
            op += 1
            st += char
    if len(st) != n:
        return 0
    return op
