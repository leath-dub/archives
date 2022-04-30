#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.split()
    line = [[i for i in wrd] for wrd in line]
    if len(line[0]) != len(line[1]):
        print(False)
    else:
        for ch in line[0]:
            if ch in line[1]:
                line[1].remove(ch)
        print(line[1] == [])
