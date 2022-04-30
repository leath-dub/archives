#!/usr/bin/env python3

t = 0
s = 0
n = int(input())
while n != 0:
    if n > 0:
        t += n
    else:
        s += n
    n = int(input())
print(s, t)
