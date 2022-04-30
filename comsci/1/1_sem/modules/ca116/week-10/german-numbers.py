#!/usr/bin/env python3

import sys

eins = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}
inp = sys.stdin.readlines()
i = 0
while i < len(inp):
    inp[i] = inp[i].rstrip()
    if inp[i] in eins:
        sys.stdout.write(eins[inp[i]] + "\n")
    i += 1
