#!/usr/bin/env python3

n = int(input())
i = 1
x = 1
y = 0
r = 0
while i < n + 1:
    print(r)
    if i <= 1:
        r = i
    else:
        r = x + y
        y = x
        x = r
    i += 1
