#!/usr/bin/env python3

import sys

FILE = sys.argv[1]
tnumal = {}
with open(FILE, "r") as f:
    for line in f.readlines():
        tnumal[line.split()[0]] = line.split()[1]
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
    print(" ".join([tnumal[numal[int(s)]] if s.isnumeric() and int(s) in range(0, 11) else "unknown" for s in line.strip().split()]))
