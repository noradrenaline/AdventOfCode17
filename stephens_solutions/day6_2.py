#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622

"""
Out of curiosity, the debugger would also like to know the size of the loop:
starting from a state that has already been seen, how many block redistribution
cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer
in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in
your puzzle input?
"""

import fileinput


def argmax(bins):
    return max(zip(range(len(bins)), bins),
               key=lambda x: x[1])[0]


def pull_max(bins):
    max_bin, max_val = (argmax(bins), max(bins))
    return (max_bin,
            max_val,
            tuple(i for i in bins[:max_bin]) + (0,) +
            tuple(i for i in bins[max_bin + 1:]))


def redistribute(bin, val, bins):
    idx = (bin + 1) % len(bins)
    bins_list = list(bins)
    while val > 0:
        bins_list[idx] += 1
        val -= 1
        idx = (idx + 1) % len(bins)
    return tuple(bins_list)


def count_cycles(bins):
    memory = {}
    cycle = 0
    while bins not in memory:
        cycle += 1
        memory[bins] = cycle
        bins = redistribute(*pull_max(bins))
    return cycle - memory[bins] + 1


print count_cycles(tuple(int(i)
                         for i in fileinput.input().readline().strip().split()))
