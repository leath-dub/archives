#!/usr/bin/env python3

deci = int(input())
r = ""
check = 0
hexref = "0123456789abcdef"
while deci > 0:
    check = deci % 16
    r = hexref[check] + r
    deci = deci // 16
print(r)
