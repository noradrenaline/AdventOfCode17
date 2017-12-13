#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621, W0603

r"""
This heredoc broke my atom's python parser
"""
import fileinput

class String(object):
    def __init__(self, size):
        self.string = range(size)
        self.pos = 0
        self.skip = 0
    def reverse(self, value):
        self._reverse(self.pos, value)
        self.pos += value + self.skip
        self.pos = self.pos % len(self.string)
        self.skip += 1
    def _swap(self, i, j):
        tmp = self.string[i]
        self.string[i] = self.string[j]
        self.string[j] = tmp
    def _reverse(self, offs, value):
        indexes = [(offs + i) % len(self.string) for i in range(value)]
        for i in range(len(indexes)/2):
            self._swap(indexes[i], indexes[-(i+1)])

string = String(256)
for line in fileinput.input():
    for val in line.strip().split(','):
        string.reverse(int(val))

print string.string[0] * string.string[1]
