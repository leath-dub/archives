#!/usr/bin/env python3

deci = int(input())
r = ""
while deci != 0:
    r = str(deci % 2) + r
    deci //= 2
print(r)
