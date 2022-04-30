#!/usr/bin/env python3

import sys

FILE = sys.argv[1]
d = {}
with open(FILE, "r") as f:
    line = f.readline().strip()
    while line != "":
        d[line.split()[0]] = tuple(line.split()[1:])
        line = f.readline().strip()
for name in sys.stdin:
    try:
        print("Name:", name.strip())
        print("Phone:", d[name.strip()][0])
        print("Email:", d[name.strip()][1])
    except KeyError:
        print("No such contact")
