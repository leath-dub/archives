#!/usr/bin/env python3

t = 0
n = int(input())
while n != 0:
    if n > 0:
        t += n
    else:
        t = t + (n * -1)
    n = int(input())
print(t)
