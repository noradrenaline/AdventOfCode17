#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301, R0903, W0622, W0621, W0603

r"""
Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the
garbage. The leading and trailing < and > don't count, nor do any canceled
characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input?
"""

import fileinput
from collections import defaultdict
SCORE = 0
STACK = 0
CANCEL = False
GARBAGE = False
GARBAGE_COUNT = 0


def canceller(f):
    def g():
        global CANCEL
        if CANCEL:
            CANCEL = False
            return
        return f()
    return g


@canceller
def in_stack():
    global STACK, GARBAGE, GARBAGE_COUNT
    if not GARBAGE:
        STACK += 1
    else:
        GARBAGE_COUNT += 1


@canceller
def out_stack():
    global STACK, SCORE, GARBAGE, GARBAGE_COUNT
    if not GARBAGE:
        SCORE += STACK
        STACK -= 1
    else:
        GARBAGE_COUNT += 1


@canceller
def in_garbage():
    global GARBAGE, GARBAGE_COUNT
    GARBAGE_COUNT += 1 if GARBAGE else 0
    GARBAGE = True


@canceller
def out_garbage():
    global GARBAGE
    GARBAGE = False


@canceller
def saw_canceller():
    global CANCEL, GARBAGE
    CANCEL = True if GARBAGE else False

@canceller
def otro():
    global GARBAGE_COUNT
    GARBAGE_COUNT += 1 if GARBAGE else 0

LU = defaultdict(lambda: otro,
                 {
                     "{": in_stack,
                     "}": out_stack,
                     "<": in_garbage,
                     ">": out_garbage,
                     "!": saw_canceller
                 })
for char in fileinput.input().readline().strip():
    LU[char]()
print GARBAGE_COUNT
