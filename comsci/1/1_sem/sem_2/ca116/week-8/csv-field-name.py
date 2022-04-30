#!/usr/bin/env python3

from sys import argv

arg = int(argv[1])

s = input()
commas = 0
i = 0
while commas < arg:
    if s[i] == ",":
        commas += 1
    i += 1
old = i
while i < len(s) and s[i] != ",":
    i += 1
if i < len(s):
    print(s[old:i])
else:
    print(s[old:])
