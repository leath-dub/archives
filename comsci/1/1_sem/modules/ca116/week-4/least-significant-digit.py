#!/usr/bin/env python3

i = 0
t = 0
while i < 10:
    x = int(input())
    if x < 0:
        x *= -1
    if x % 10 < (x % 100) // 10:
        t += x
    else:
        t += (x % 100) // 10
    i += 1
print(t)
