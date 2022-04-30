#!/usr/bin/env python3

n = int(input())

if n % 2 == 0:
    n //= 2
    print(n)
else:
    n *= 3
    print(n + 1)
