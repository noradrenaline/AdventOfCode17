#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621

r"""
You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series of
unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions
look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it
is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the registers
are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in
your puzzle input?
"""

import fileinput
from collections import namedtuple

Instruction = namedtuple('Instruction',
                         ['register', 'direction', 'amount', 'cond_register', 'relation', 'val'])


def parse_instruction(line):
    register, direction, amount, _, cond_register, relation, val = line.split()
    return Instruction(register, direction, int(amount), cond_register, relation, int(val))


class Register(object):
    def __init__(self, name):
        self.name = name
        self.value = 0


def init_program(lines):
    program = [parse_instruction(line) for line in lines]
    registers = {j: Register(j)
                 for j in set([i.register for i in program] +
                              [i.cond_register for i in program])}
    return (program, registers)


def eval_instruction(instruction, registers):
    if eval('{} {} {}'.format(registers[instruction.cond_register].value,
                              instruction.relation,
                              instruction.val)):
        registers[instruction.register].value += instruction.amount * \
            (1 if instruction.direction == 'inc' else -1)


program, registers = init_program(fileinput.input())
for instruction in program:
    eval_instruction(instruction, registers)
print max(registers.values(), key=lambda x: x.value).value
