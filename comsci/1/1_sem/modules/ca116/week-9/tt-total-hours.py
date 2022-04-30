#!/usr/bin/env python3

total = 0
s = input()
while s != "end":
    total += int(s.split()[2])
    s = input()
print(total)
