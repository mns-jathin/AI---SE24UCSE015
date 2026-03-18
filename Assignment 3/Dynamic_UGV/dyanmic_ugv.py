#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:07:30 2026

@author: jathinmadineni
"""

import heapq
import random
import time
import math
import copy

"""
Unlike static code, which plans only once at the beginning, this dynamic code continuously senses the environment and replans the path whenever new obstacles are detected.
Static code makes the assumption that the environment never changes, whereas it manages changing conditions (new obstacles appearing during movement).
Because of the frequent replanning, dynamic navigation is therefore more adaptable and realistic, but it requires more processing power.
"""
GRID_ROWS = 70
GRID_COLS = 70
FREE = 0
BLOCKED = 1
SENSOR_RANGE = 5
OBSTACLE_CHANCE = 0.03

def calc_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

MOVES = [
    (-1, 0, 1.0), (1, 0, 1.0),
    (0, -1, 1.0), (0, 1, 1.0),
    (-1, -1, 1.414), (-1, 1, 1.414),
    (1, -1, 1.414), (1, 1, 1.414)
]

def neighbours(r, c):
    nbs = []
    for dr, dc, cost in MOVES:
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < GRID_ROWS and nc >= 0 and nc < GRID_COLS:
            nbs.append((nr, nc, cost))
    return nbs

def find_path(grid, start, goal):
    g_scores = {start: 0.0}
    pq = [(calc_dist(start, goal), 0.0, start)]
    came_from = {}
    visited_nodes = set()

    while pq:
        f, g, current = heapq.heappop(pq)
        if current in visited_nodes:
            continue
        visited_nodes.add(current)

        if current == goal:
            path = []
            cur = goal
            while cur != start:
                path.append(cur)
                cur = came_from.get(cur)
                if cur is None:
                    return []
            path.append(start)
            path.reverse()
            return path

        for nr, nc, move_cost in neighbours(current[0], current[1]):
            nb = (nr, nc)
            if grid[nr][nc] == BLOCKED:
                continue
            tentative_g = g + move_cost
            if tentative_g < g_scores.get(nb, float("inf")):
                g_scores[nb] = tentative_g
                came_from[nb] = current
                h = calc_dist(nb, goal)
                heapq.heappush(pq, (tentative_g + h, tentative_g, nb))

    return []

class UGV:

    def __init__(self, real_map, start, goal, sensor_range=SENSOR_RANGE, seed=99):
        self.real_map = real_map
        self.start = start
        self.goal = goal
        self.pos = start
        self.sensor_range = sensor_range
        self.known = [[FREE]*GRID_COLS for _ in range(GRID_ROWS)]
        self.known[goal[0]][goal[1]] = FREE
        self.path = []
        self.history = [start]
        self.steps = 0
        self.replans = 0
        self.dist = 0.0
        random.seed(seed)

    def scan(self):
        r, c = self.pos
        found_problem = False
        path_cells = set(self.path)

        for rr in range(max(0, r - self.sensor_range), min(GRID_ROWS, r + self.sensor_range + 1)):
            for cc in range(max(0, c - self.sensor_range), min(GRID_COLS, c + self.sensor_range + 1)):
                if calc_dist((r, c), (rr, cc)) <= self.sensor_range:
                    if self.real_map[rr][cc] == BLOCKED and self.known[rr][cc] == FREE:
                        self.known[rr][cc] = BLOCKED
                        if (rr, cc) in path_cells:
                            found_problem = True
        return found_problem

    def add_random_obstacles(self):
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                cell = (r, c)
                if cell == self.start or cell == self.goal or cell == self.pos:
                    continue
                if self.real_map[r][c] == FREE:
                    if random.random() < (OBSTACLE_CHANCE / (GRID_ROWS * GRID_COLS)) * 100:
                        self.real_map[r][c] = BLOCKED

    def step_forward(self):
        if len(self.path) < 2:
            return None

        nxt = self.path[1]
        step_cost = calc_dist(self.pos, nxt)

        self.dist += step_cost
        self.pos = nxt
        self.path = self.path[1:]

        self.history.append(nxt)
        self.steps += 1

        return nxt

    def run(self, max_steps=5000):
        print(f"starting ugv from {self.start} -> {self.goal}")
        print(f"(sensor={self.sensor_range}, randomness={OBSTACLE_CHANCE})")

        self.path = find_path(self.known, self.pos, self.goal)

        if not self.path:
            print("no path found at start")
            return False

        t0 = time.perf_counter()

        for i in range(max_steps):
            blocked = self.scan()

            if blocked:
                self.replans += 1
                self.path = find_path(self.known, self.pos, self.goal)
                if not self.path:
                    print(f"stopped at step {i}, no path anymore")
                    break

            new_pos = self.step_forward()

            if new_pos is None:
                print("ran out of path")
                break

            if self.pos == self.goal:
                elapsed = (time.perf_counter() - t0) * 1000
                print("reached goal")
                self.report(elapsed, True)
                return True

            self.add_random_obstacles()

        elapsed = (time.perf_counter() - t0) * 1000
        print("timeout or failed")
        self.report(elapsed, False)
        return False

    def report(self, elapsed, success):
        straight = calc_dist(self.start, self.goal)
        efficiency = (straight / self.dist * 100) if self.dist > 0 else 0
        known_obs = sum(self.known[r][c] for r in range(GRID_ROWS) for c in range(GRID_COLS))

        print("result:", "success" if success else "fail")
        print("steps:", self.steps)
        print("distance:", round(self.dist, 2))
        print("efficiency:", round(efficiency, 1), "%")
        print("replans:", self.replans)
        print("known obstacles:", known_obs)
        print("time (ms):", round(elapsed, 2))


if __name__ == "__main__":

    print("="*50)
    print("ugv simulation (dynamic obstacles)")
    print("="*50)

    random.seed(42)

    base_map = []
    for _ in range(GRID_ROWS):
        row = []
        for _ in range(GRID_COLS):
            if random.random() < 0.2:
                row.append(BLOCKED)
            else:
                row.append(FREE)
        base_map.append(row)

    start = (2, 2)
    goal = (67, 67)

    base_map[start[0]][start[1]] = FREE
    base_map[goal[0]][goal[1]] = FREE

    robot = UGV(copy.deepcopy(base_map), start, goal)

    robot.run()

 