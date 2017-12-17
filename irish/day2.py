#!/usr/bin/env python3
'''
Day 2: Corruption Checksum

Part 1:

The spreadsheet consists of rows of apparently-random numbers. To make sure the
recovery process is on the right track, they need you to calculate the
spreadsheet's checksum. For each row, determine the difference between the
largest value and the smallest value; the checksum is the sum of all of these
differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

The first row's largest and smallest values are 9 and 1, and their difference
is 8.

The second row's largest and smallest values are 7 and 3, and their difference
is 4.

The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

Part 2:

It sounds like the goal is to find the only two numbers in each row where one
evenly divides the other - that is, where the result of the division operation
is a whole number. They would like you to find those numbers on each line,
divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

In the first row, the only two numbers that evenly divide are 8 and 2; the
result of this division is 4.

In the second row, the two numbers are 9 and 3; the result is 3.

In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
'''

import argparse
import csv
import itertools


def part1(data):
	'''Calculate checksum of data (a CSV reader) by summing the differences of
	the highest and lowest values in each row.'''
	# Accumulator for deltas
	checksum = 0

	print('Max\tMin\tDelta')
	for row in data:
		# Coerce strings to ints when checking for max and min
		r_max = int(max(row, key=int))
		r_min = int(min(row, key=int))
		delta = r_max - r_min
		print('{}\t{}\t{}'.format(r_max, r_min, delta))
		checksum += delta

	return checksum


def part2(data):
	'''Calculate checksum of data (a CSV reader) by summing the the quotients
	of the only two values in each row which where the smaller value is a
	proper factor of the larger value.'''
	# Accumulator for deltas
	checksum = 0

	print('Dividend\tDivisor\tQuotient')
	for row in data:
		# Coerce strings to ints
		prod = [x for x in itertools.product(row, row[1:])
				if int(x[0]) > int(x[1]) and int(x[0]) % int(x[1]) == 0]
		dividend = int(prod[0][0])
		divisor = int(prod[0][1])
		quotient = int(dividend / divisor)
		checksum += quotient
		print('{}\t\t{}\t{}'.format(dividend, divisor, quotient))

	return checksum


def main():
	PARSER = argparse.ArgumentParser(description='')
	PARSER.add_argument('file_path', metavar='FILE', type=str,
			help='Path to input file')
	ARGS = PARSER.parse_args()

	with open(ARGS.file_path) as f:
		data = csv.reader(f, delimiter='\t')
		part1_checksum = part1(data)
		# Return to beginning of file
		f.seek(0)
		part2_checksum = part2(data)

	print('Checksum 1: {}'.format(part1_checksum))
	print('Checksum 2: {}'.format(part2_checksum))


if __name__ == '__main__':
	main()


# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
