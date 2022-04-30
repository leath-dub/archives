#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(s)
    s = input()
i = 0
while i < len(a):
    j = i
    while j < len(a):
        if a[j] < a[i]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        j += 1
    print(a[i])
    i += 1
