#!/usr/bin/env python3

i = 0
te = 0
while i < 10:
    x = int(input())
    te += x * ((x - 1) % 2)
    i += 1
print(te)
