#!/usr/bin/env python3

n = int(input())
m = int(input())
x = m
i = 0
while i < n:
    print(x)
    x = ((x - 1) % 2) * (x // 2) + (x % 2) * (3 * x + 1))
    i += 1
