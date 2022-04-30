#!/usr/bin/env python3

a_dict = {}
intersection = {}

with open("a.txt") as a:
    with open("b.txt") as b:

        line = a.readline().rstrip()
        while 0 < len(line):
            a_dict[line] = None
            line = a.readline().rstrip()

        line = b.readline().rstrip()
        while 0 < len(line):
            if line in a_dict:
                intersection[line] = None
            line = b.readline().rstrip()

for element in intersection:
    print(element)
