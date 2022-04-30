#!/usr/bin/env python3

s = input()
i = 0
j = 0
while i < len(s):
    j = j + int(s[i])
    i += 1
print(j)
