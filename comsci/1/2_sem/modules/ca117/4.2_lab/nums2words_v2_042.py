#!/usr/bin/env python3

import sys

numal = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
]
for line in sys.stdin:
    print(" ".join([numal[int(s)] if s.isnumeric() and int(s) in range(0, 11) else "unknown" for s in line.strip().split()]))
