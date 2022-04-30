#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()
p = 0
i = 0
while i < len(a):
    if a[i] < a[p]:
        p = i
    i += 1
print(p)
