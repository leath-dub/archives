#!/usr/bin/env python3

n = int(input())
x = 1
y = 0
r = 0
i = 0
while r < n:
    if i > 0:
        print(r)
    if i <= 1:
        r = i
    else:
        r = x + y
        y = x
        x = r
    i += 1
