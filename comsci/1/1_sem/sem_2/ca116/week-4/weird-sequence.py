#!/usr/bin/env python3

n = int(input())
i = 0
x = 0
while i < n:
    print(x)
    x = (x % 2) * (x + (x * - 2) + 1) + ((x - 1) % 2) * (x - (x * 2) - 1)
    i += 1
