#!/usr/bin/env python3

a = 1000 * [""]
b = 1000 * [0]
s = input()
while s != "end":
    a[int(s)] = s
    b[int(s)] += 1
    s = input()
i = 0
j = 0
while i < 1000:
    if a[i] != "":
        print(a[i])
    if not(j >= 1 and j <= b[i]):
        j = b[i]
    if j > 1:
        j -= 1
        i -= 1
    i += 1
