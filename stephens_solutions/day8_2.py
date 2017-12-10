#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621

r"""
To be safe, the CPU also needs to know the highest value held in any register
during this process so that it can decide how much memory to allocate to these
operations. For example, in the above instructions, the highest value ever held
was 10 (in register c after the third instruction was evaluated).
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
max_val = -1
for instruction in program:
    max_val = max(max_val, max(registers.values(), key=lambda x: x.value).value)
    eval_instruction(instruction, registers)
max_val = max(max_val, max(registers.values(), key=lambda x: x.value).value)
print max_val
