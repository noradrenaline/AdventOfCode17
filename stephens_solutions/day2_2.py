#!/usr/bin/env python

"""
"Great work; looks like we're on the right track after all. Here's a star for
your effort." However, the program seems a little worried. Can programs be
worried?

"Based on what we're seeing, it looks like all the User wanted is some
information about the evenly divisible values in the spreadsheet.
Unfortunately, none of us are equipped for that kind of calculation - most of
us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one
evenly divides the other - that is, where the result of the division operation
is a whole number. They would like you to find those numbers on each line,
divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2;
    the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
"""

import fileinput
import itertools


def is_divisible(x, y):
    return max(x, y) % min(x, y) == 0

def order_div(x, y):
    return max(x, y) / min(x, y)

def get_cell(row):
    nums = [int(row) for row in row.split()]
    lnums = zip(xrange(len(nums)), nums)
    return [order_div(i[0][1], i[1][1])
            for i in itertools.product(lnums, lnums)
            if i[0][0] < i[1][0] and is_divisible(i[0][1], i[1][1])][0]

print sum([get_cell(line) for line in fileinput.input()])
