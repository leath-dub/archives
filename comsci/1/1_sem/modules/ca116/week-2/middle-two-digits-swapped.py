#!/usr/bin/env python3

n = int(input())
print((n % 10000 % 1000 // 100) * 10 + n % 10000 // 1000)
