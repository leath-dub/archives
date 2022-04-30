#!/usr/bin/env python3

i = 0
t = 0
while i < 10:
    x = int(input())
    if x < 0:
        x *= -1
    t += (x % 10)
    i += 1
print(t)
