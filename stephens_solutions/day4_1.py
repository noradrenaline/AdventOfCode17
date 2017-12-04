#!/usr/bin/env python

# pylint: disable=C0103, C0111, C0301

"""
A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""

import fileinput
import collections


def wc(lines):
    for line in lines:
        wc_d = collections.defaultdict(int)
        for w in line.strip().split():
            wc_d[w] += 1
        yield len([j for j in wc_d.itervalues() if j > 1])


print sum([1 for i in wc(fileinput.input()) if i == 0])
