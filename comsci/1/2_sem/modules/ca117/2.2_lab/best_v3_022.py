#!/usr/bin/env python3

import sys

larg = [0, ""]
FILE = sys.argv[1]
try:
    with open(FILE) as f:
        s = f.readline()
        while len(s) > 0:
            pair = s.split()
            try:
                mark = int(pair[0])
            except ValueError:
                print(f'Invalid mark {pair[0]} encountered. Skipping.')
            if mark > larg[0]:
                larg[0] = mark
                larg[1] = " ".join(pair[1:])
            s = f.readline()
    print(f'Best student: {larg[1]:s}')
    print(f'Best mark: {larg[0]:d}')
except FileNotFoundError:
    print(f'The file {FILE} could not be opened')
