#!/usr/bin/env python3

s = input()
i = 0
while i < len(s):
    if "A" <= s[i] and s[i] <= "Z":
        print(i)
        i = len(s)
    i += 1
