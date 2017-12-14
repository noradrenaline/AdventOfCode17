#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621, W0603

r"""
How many steps away is the furthest he ever got from his starting position?
"""
import fileinput

CUBE_DIRS = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}

x, y, z = (0, 0, 0)

def cube_dist(x, y, z):
    return (abs(x)+abs(y)+abs(z))/2

d_max = 0

for line in fileinput.input():
    for direction in line.strip().split(','):
        dx, dy, dz = CUBE_DIRS[direction]
        x, y, z = (x + dx, y + dy, z + dz)
        d_max = max(d_max, cube_dist(x, y, z))

print d_max
