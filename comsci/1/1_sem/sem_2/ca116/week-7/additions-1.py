#!/usr/bin/env python3

i = 0
while i < 10:
    s = input()
    j = 0
    while j < len(s) and not(s[j] == "+"):
        j += 1
    if j < len(s):
        print(int(s[j + 1:]) + int(s[:j]))
    else:
        print(s)
    i += 1
