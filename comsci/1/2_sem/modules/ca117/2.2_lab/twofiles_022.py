#!/usr/bin/env python3

import sys

FILE_1 = sys.argv[1]
FILE_2 = sys.argv[2]

with open(FILE_1) as f1:
    with open(FILE_2) as f2:
        n = f1.readline()
        m = f2.readline()
        while len(n) > 0:
            sys.stdout.write(n)
            sys.stdout.write(m)
            n = f1.readline()
            m = f2.readline()
