#!/usr/bin/env python3

import sys

x_y = []

inp = sys.stdin.readline()
while 0 < len(inp):
    x_y.append(inp)
    inp = sys.stdin.readline()
print(" " + "-" * 20)
i = 0
while i < 20:
    inverse_i = 19 - i
    lst = [" "] * 20
    k = 0
    while k < len(x_y):
        split = x_y[k].split()
        if int(split[1]) == inverse_i:
            lst[int(split[0])] = "*"
        k += 1
    sys.stdout.write("|")
    j = 0
    while j < 20:
        sys.stdout.write(lst[j])
        j += 1
    sys.stdout.write("|\n")
    i += 1
print(" " + "-" * 20)
