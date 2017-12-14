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
    def dense(self):
        return ''.join([format(reduce(lambda x, y: x^y,
                                      [self.string[j]
                                       for j in range(i*16, (i+1)*16)]),
                               '02x')
                        for i in range(16)])

string = String(256)
for line in fileinput.input():
    for n in xrange(64):
        for val in [ord(i) for i in line.strip()] + [17, 31, 73, 47, 23]:
            string.reverse(val)

print string.dense()
