#!/usr/bin/env python3
'''
Day 2: Corruption Checksum

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
'''

import argparse
import csv


def main():
	PARSER = argparse.ArgumentParser(description='')
	PARSER.add_argument('file_path', metavar='FILE', type=str,
			help='Path to input file')
	ARGS = PARSER.parse_args()

	# Accumulator for deltas
	checksum = 0

	# Read input
	with open(ARGS.file_path) as f:
		data = csv.reader(f, delimiter='\t')
		print('Max\tMin\tDelta')
		for row in data:
			# Coerce strings to ints when checking for max and min
			r_max = int(max(row, key=int))
			r_min = int(min(row, key=int))
			delta = r_max - r_min
			print('{}\t{}\t{}'.format(r_max, r_min, delta))
			checksum += delta

	print('Checksum: {}'.format(checksum))


if __name__ == '__main__':
	main()


# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
