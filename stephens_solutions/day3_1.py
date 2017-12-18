#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301


"""
You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must
be carried back to square 1 (the location of the only access port for this
memory system) by programs that can only move up, down, left, or right. They
always take the shortest path: the Manhattan Distance between the location of
the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?

Your puzzle input is 368078.

"""
import sys
from math import floor, ceil
import itertools


def get_square(x):
    return int(floor(ceil(x**0.5) / 2.0))

def odd(x):
    return x * 2 + 1

def edge_traipse(start, limit):
    direction = -1 if start > 0 else 1
    x = start
    while True:
        yield x
        x += direction
        if x >= limit or x == 0:
            direction = -direction

def get_pos_on_square(x):
    n = get_square(x)
    s = odd(n)
    p = x - odd(n-1)**2 - 1
    if n > 0:
        return list(itertools.islice(edge_traipse(n-1, n), s**2-1))[p] + n
    return 0

print get_pos_on_square(int(sys.argv[1]))