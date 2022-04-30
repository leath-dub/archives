#!/usr/bin/env python3

import sys

fruit = {
    "apple": None,
    "banana": None,
    "cherry": None,
    "orange": None,
    "pear": None,
}
i = 0
inp = sys.stdin.readlines()
while i < len(inp):
    inp[i] = inp[i].rstrip()
    if inp[i] in fruit:
        sys.stdout.write(inp[i] + "\n")
    i += 1
