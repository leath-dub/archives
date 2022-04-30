#!/usr/bin/env python3

s = input()
pluses = 0
total = 0
while pluses != 4:
    i = 0
    while i < len(s) and s[i] != "+":
        i += 1
    if i < len(s):
        pluses += 1
        total += int(s[:i])
        s = s[i + 1:]
print(total + int(s))
