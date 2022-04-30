#!/usr/bin/env python3

deci_index = [""]
deci_index *= 10
s = input()
while s != "end":
    deci_index[int(s)] += "*"
    s = input()
i = 0
while i < len(deci_index):
    print(i, deci_index[i])
    i += 1
