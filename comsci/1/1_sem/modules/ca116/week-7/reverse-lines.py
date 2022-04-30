#!/usr/bin/env python3

rev = []
norm = []
s = input()
while s != "end":
    norm.append(s)
    rev.append(s)
    s = input()
i = 0
while i < len(norm):
    print(rev[len(norm) - i - 1])
    i += 1
