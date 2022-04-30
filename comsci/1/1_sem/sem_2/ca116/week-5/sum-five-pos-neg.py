#!/usr/bin/env python3

i = 0
t = 0
s = 0
n = 0
while i < 5:
    n = int(input())
    if n > 0:
        t += n
    else:
        s += n
    i += 1
print(s, t)
