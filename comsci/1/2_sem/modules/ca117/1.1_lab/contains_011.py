#!/usr/bin/env python3

import sys

for line in sys.stdin:
    first = line.split()[0].lower()
    second = line.split()[1].lower()
    check = {}
    contains = True
    for ch in second:
        check[ch] = True
    for ch in first:
        if ch in check and check[ch] is False:
            contains = False
        if ch in check:
            check[ch] = False
    print(contains)
