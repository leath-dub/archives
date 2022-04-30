#!/usr/bin/env python3

s = input()
total = 0
while len(s) > 1:
    i = 0
    while i < len(s) and s[i] != "+":
        i += 1
    if i < len(s):
        print(s[:i])
        total += int(s[:i])
        s = s[i + 1:]
    print(s)
print(total + int(s))
