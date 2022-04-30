#!/usr/bin/env python3

import sys

d = {
    "!": True,
    ".": True,
    "?": True,
}
inp = sys.stdin.read()
a = inp.split()
s = ""
i = 0
while i < len(a):
    if len(a[i]) > 0 and a[i][len(a[i]) - 1] in d:
        s += a[i]
        print(s)
        s = ""
    else:
        s += a[i] + " "
    i += 1
