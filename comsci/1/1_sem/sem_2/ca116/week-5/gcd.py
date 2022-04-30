#!/usr/bin/env python3

a = int(input())
b = int(input())
while b > 0:
    oldb = b
    b = a % b
    a = oldb
print(a)
