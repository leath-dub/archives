#!/usr/bin/env python3

even = []
odd = []
s = input()
while s != "end":
    if int(s) % 2 == 0:
        even.append(s)
    else:
        odd.append(s)
    s = input()
even = even + odd
i = 0
while i < len(even):
    print(even[i])
    i += 1
