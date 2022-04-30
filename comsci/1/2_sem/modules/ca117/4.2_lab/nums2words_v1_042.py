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
    print(" ".join([numal[int(s)] for s in line.strip().split()]))
