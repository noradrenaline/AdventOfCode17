#!/usr/bin/env python
import sys
from collections import deque
A = sys.argv[1]
B = deque(sys.argv[1])
B.rotate()
print sum([int(i[0]) for i in zip(A,B) if i[0] == i[1]])
