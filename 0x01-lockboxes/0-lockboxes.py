#!/usr/bin/python3
""" A module to implement lockboxes """ 
from collections import deque


def canUnlockAll(boxes):
    """ A function that determines if all the boxes can be opened """
    queue = deque([0])
    visited = set([0])
    while queue:
        node = queue.popleft()
        for child in boxes[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return len(visited) == len(boxes)
