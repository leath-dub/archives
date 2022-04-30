#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(s)
    s = input()
s = input()
i = 0
while i < len(a):
    print(int(a[i]) + int(s))
    i += 1
