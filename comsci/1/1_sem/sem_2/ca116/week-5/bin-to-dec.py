#!/usr/bin/env python3

n = int(input())
result = 0
pwr = 1
while n > 0:
    result += (n % 10) * pwr
    n //= 10
    pwr *= 2

print(result)
