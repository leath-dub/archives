#!/usr/bin/env python3

import sys

def max_discount():
    a = sys.stdin.readlines()
    a = a[1]
    a = a.rstrip()
    a = a.split()
    i = 0 
    out = 0
    a.sort(reverse=True)
    while i < len(a):
        if i % 3 == 2:
            out += int(a[i])
        i += 1
    return print(str(out))
max_discount()
