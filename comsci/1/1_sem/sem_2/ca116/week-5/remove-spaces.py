#!/usr/bin/env python3

s = input()
i = 0
t = ""
while i < len(s):
    if s[i] == " ":
        i = i
    else:
        t += s[i]
    i += 1
print(t)
