#!/usr/bin/env python3

f = input()
neg = ""
if f[0] == "-":
    neg = "-"
    f = f[1:]
if f[0] == ".":
    f = "0" + f
elif f[len(f) - 1] == ".":
    f += "0"
else:
    i = 0
    while i < len(f) and f[i] != ".":
        i += 1
    if i == len(f):
        f += ".0"
print(neg + f)
