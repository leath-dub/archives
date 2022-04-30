#!/usr/bin/env python3

import sys

d = {}

with open("translation.txt") as trans:
    f_in = trans.readline()
    while 0 < len(f_in):
        f_in = f_in.rstrip()
        f_in = f_in.split()
        d[f_in[0]] = f_in[1]
        f_in = trans.readline()

inp = sys.stdin.readlines()
i = 0
while i < len(inp):
    inp[i] = inp[i].rstrip()
    if inp[i] in d:
        sys.stdout.write(d[inp[i]] + "\n")
    i += 1
