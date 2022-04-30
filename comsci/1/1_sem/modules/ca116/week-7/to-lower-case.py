#!/usr/bin/env python3

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

s = input()
while s != "end":
    tmp = ""
    i = 0
    while i < len(s):
        if "A" <= s[i] and s[i] <= "Z":
            j = 0
            while j < len(upper):
                if s[i] == upper[j]:
                    tmp += lower[j]
                j += 1
        else:
            tmp += s[i]
        i += 1
    print(tmp)
    s = input()
