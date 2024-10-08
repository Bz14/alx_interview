#!/usr/bin/python3
""" A module to implement lockboxes """ 
from collections import defaultdict


def canUnlockAll(boxes):
    """ A function that determines if all the boxes can be opened """
    visited = set([0])
    def DFS(node):
        for child in boxes[node]:
            if child not in visited:
                visited.add(child)
                DFS(child)
    
    DFS(0)
    return len(visited) == len(boxes)
