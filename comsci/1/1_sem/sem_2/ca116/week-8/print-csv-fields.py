#!/usr/bin/env python3

a = []
s = "," + input() + ","
while s != ",end,":
    i = 0
    tag = 0
    while i < len(s):
        if s[i] == ",":
            tmp = s[tag:i]
            a.append(tmp[1:])
            tag = i
        i += 1
    s = "," + input() + ","
i = int(input()) + 1
while i < len(a):
    print(a[i])
    i += 4
