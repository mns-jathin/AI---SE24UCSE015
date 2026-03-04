#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:58:49 2026

@author: jathinmadineni
"""

from collections import deque
import heapq

start = (3, 3, 0)   
goal = (0, 0, 1)

def safe(position):
    m_left, c_left, boat = position
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True

def next_moves(position):
    m_left, c_left, boat = position
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    children = []

    for m, c in moves:
        if boat == 0:
            new_position = (m_left - m, c_left - c, 1)
        else:
            new_position = (m_left + m, c_left + c, 0)

        if safe(new_position):
            children.append(new_position)

    return children


#BFS
def bfs():
    line = deque([(start, [])])
    visited = set()

    while line:
        current, path = line.popleft()

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for child in next_moves(current):
                line.append((child, path + [current]))


#Uniform cost search
def ucs():
    heap = []
    heapq.heappush(heap, (0, start, []))
    visited = set()

    while heap:
        cost, current, path = heapq.heappop(heap)

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for child in next_moves(current):
                heapq.heappush(heap, (cost + 1, child, path + [current]))


#DFS 
def dfs():
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for child in next_moves(current):
                stack.append((child, path + [current]))

#Depth limited search
def dls(current, limit, path, visited):
    if current == goal:
        return path + [current]

    if limit == 0:
        return None

    visited.add(current)

    for child in next_moves(current):
        if child not in visited:
            result = dls(child, limit - 1, path + [current], visited)
            if result:
                return result

    visited.remove(current)  
    return None


#iterative deepening DFS 
def iddfs(max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, depth, [], set())
        if result:
            return result

#we are running everything now 
print("BFS solution:")
print(bfs())

print("\nUniform Cost Search solution:")
print(ucs())

print("\nDFS solution:")
print(dfs())

print("\nDepth Limited Search where limit is 12:")
print(dls(start,12,[],set()))

print("\nIterative Deepening DFS:")
print(iddfs(12))

print("BFS uses a lot of memory but is quick for the shortest solution because all costs are the same, UCS and BFS are identical in this case.DFS may not provide the shortest solution, but it uses less memory.IDDFS provides the best balance between optimal like BFS and low memory like DFS.")
