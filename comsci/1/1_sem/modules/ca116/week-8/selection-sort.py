#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()
j = 0
while j < len(a):
    i = j
    while i < len(a):
        if a[i] < a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        i += 1
    print(a[j])
    j += 1
