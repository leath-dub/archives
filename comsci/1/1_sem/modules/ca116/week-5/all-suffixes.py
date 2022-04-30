#!/usr/bin/env python3

s = input()
i = 0
print(s)
while i < len(s) - 1:
    print(s[i + 1:])
    i += 1
