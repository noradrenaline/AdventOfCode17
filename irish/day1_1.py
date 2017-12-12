#!/usr/bin/env python3
'''
Day 1: Inverse Captcha

Part 1:

The captcha requires you to review a sequence of digits (your puzzle input) and
find the sum of all digits that match the next digit in the list. The list is
circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second
digit and the third digit (2) matches the fourth digit.

1111 produces 4 because each digit (all 1) matches the next.

1234 produces 0 because no digit matches the next.

91212129 produces 9 because the only digit that matches the next one is the
last digit, 9.

What is the solution to your captcha?

Part 2:

Now, instead of considering the next digit, it wants you to consider the digit
halfway around the circular list. That is, if your list contains 10 items, only
include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit
2 items ahead.

1221 produces 0, because every comparison is between a 1 and a 2.

123425 produces 4, because both 2s match each other, but no other digit has a
match.

123123 produces 12.

12131415 produces 4.
'''

import argparse
from collections import deque


def shift(sequence, offset):
	'''Create circular list from sequence wrapped by offset.'''
	shifted = deque(sequence)
	shifted.rotate(offset)
	return (sequence, shifted)


def process(l1, l2):
	'''Find sum of all list elements with matching values one offset apart'''
	return sum([int(i[0]) for i in zip(l1, l2) if i[0] == i[1]])


def main():
	PARSER = argparse.ArgumentParser(description='')
	PARSER.add_argument('file_path', metavar='FILE', type=str,
			help='Path to input file')
	ARGS = PARSER.parse_args()

	# Read input
	with open(ARGS.file_path) as f:
		data = f.read().strip()

	# Create a second list which wraps the first last value around
	p1_res = process(*shift(data, 1))
	p2_res = process(*shift(data, int(len(data) / 2)))

	print('Part 1: {}\nPart 2: {}'.format(p1_res, p2_res))


if __name__ == '__main__':
	main()

# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
