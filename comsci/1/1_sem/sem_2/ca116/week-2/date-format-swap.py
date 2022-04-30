#!/usr/bin/env python3

n = int(input())
p = n // 10000
op0 = p * 100
op1 = ((n - p * 10000) // 100) * 10000
op2 = n - (n // 100) * 100
print(op0 + op1 + op2)
