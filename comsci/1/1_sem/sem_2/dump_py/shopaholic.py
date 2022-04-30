#!/usr/bin/env python3

import sys

stdin = sys.stdin.readlines()
a = stdin[1]
a = a.rstrip()
a = a.split()
out = 0
i = 0
tmp = 0
while i < len(a):
    j = i
    while j < len(a):
        if int(a[j]) > int(a[i]):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        j += 1
    if i % 3 == 2:
        out += int(a[i])
    i += 1
print(out)
