#!/usr/bin/env python3

from sys import argv

arg = argv[1]
s = "," + input() + ","
commas = 0
a = []
i = 0
old = 0
while commas < 11:
    if s[i] == ",":
        commas += 1
        a.append(s[old + 1:i])
        old = i
    i += 1
i = 0
while i < len(a):
    if a[i] == arg:
        print(i - 1)
    i += 1
