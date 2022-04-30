#!/usr/bin/env python3

from sys import argv as cos

s = cos[1:]
i = 0
total = 0
while i < len(s):
    total += int(s[i])
    i += 1
print(total)
