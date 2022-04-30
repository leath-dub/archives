#!/usr/bin/env python3

import sys

names = {}

with open("boys.txt") as b_names:
    word = b_names.readline().rstrip()
    while 0 < len(word):
        names[word] = "boy"
        word = b_names.readline().rstrip()
with open("girls.txt") as g_names:
    word = g_names.readline().rstrip()
    while 0 < len(word):
        if word in names:
            names[word] = "either"
        else:
            names[word] = "girl"
        word = g_names.readline().rstrip()

inp = sys.stdin.readline().rstrip()
while 0 < len(inp):
    val = names[inp]
    print(inp + " " + val)
    inp = sys.stdin.readline().rstrip()
