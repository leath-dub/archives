#!/usr/bin/env python3

s = input()

i = 0
oldi = ""
while i < len(s) and s[i] != oldi:
    oldi = s[i]
    i += 1
if i < len(s):
    print(s[i] + s[i])
