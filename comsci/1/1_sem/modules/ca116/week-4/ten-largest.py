#!/usr/bin/env python3

j = 0
i = 0
while i < 10:
    x = int(input())
    if x > j:
        j = x
    i += 1
print(j)
