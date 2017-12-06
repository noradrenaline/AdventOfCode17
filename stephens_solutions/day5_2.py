#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903

"""
Now, the jumps are even stranger: after each jump, if the offset was three or
more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and
the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

"""

import fileinput


class Instruction(object):
    def __init__(self, val):
        self.val = val

    def step(self):
        x = self.val
        self.val += 1 if self.val < 3 else -1
        return x


def load_program(finput):
    program = {}
    lc = 0
    for line in finput:
        lc += 1
        program[lc] = Instruction(int(line))
    return program


def run_program(program):
    step = 1
    sc = 0
    while step in program:
        step += program[step].step()
        sc += 1
    return sc


print run_program(load_program(fileinput.input()))
