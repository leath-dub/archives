#!/usr/bin/env python3

union = {}

with open("a.txt") as a:
    with open("b.txt") as b:

        line = a.readline()
        while 0 < len(line):
            if line.rstrip() not in union:
                union[line.rstrip()] = None
            line = a.readline()

        line = b.readline()
        while 0 < len(line):
            if line.rstrip() not in union:
                union[line.rstrip()] = None
            line = b.readline()

for word in union:
    print(word)
