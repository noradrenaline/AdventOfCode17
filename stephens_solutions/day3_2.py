#!/usr/bin/env python

#pylint: disable=C0103, C0111, C0301

"""
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store
the value 1 in square 1. Then, in the same allocation order as shown above,
they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 368078.

"""
import sys
from math import floor, ceil


def get_square(x):
    return int(floor(ceil(x**0.5) / 2.0))


def odd(x):
    return x * 2 + 1


CELLS = {}


def edge_traipse(n):
    pos = (n, -(odd(n) / 2) + 1)
    vectors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    idx = 0
    while idx < 4:
        yield pos
        pos = (pos[0] + vectors[idx][0], pos[1] + vectors[idx][1])
        if abs(pos[0]) > odd(n) / 2 or abs(pos[1]) > odd(n) / 2:
            pos = (pos[0] - vectors[idx][0], pos[1] - vectors[idx][1])
            idx += 1
            if idx < 4:
                pos = (pos[0] + vectors[idx][0], pos[1] + vectors[idx][1])


def get_neighbors(coord):
    return [
        (coord[0] - 1, coord[1] - 1),
        (coord[0] - 1, coord[1]),
        (coord[0] - 1, coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0], coord[1] + 1),
        (coord[0] + 1, coord[1] - 1),
        (coord[0] + 1, coord[1]),
        (coord[0] + 1, coord[1] + 1)
    ]


def sum_neighbors(ngbs):
    return sum([CELLS[ngb] for ngb in ngbs if ngb in CELLS])


def get_cells():
    x = 1
    while True:
        n = get_square(x)
        if n > 0:
            for c in edge_traipse(n):
                CELLS[c] = sum_neighbors(get_neighbors(c))
                yield CELLS[c]
                x += 1
        else:
            CELLS[(0, 0)] = 1
            yield 1
            x += 1

for cell in get_cells():
    if cell > int(sys.argv[1]):
        print cell
        break
