#!/usr/bin/env python3

a_dict = {}

with open("a.txt") as a:
    with open("b.txt") as b:

        line = a.readline().rstrip()
        while 0 < len(line):
            a_dict[line] = None
            line = a.readline().rstrip()

        line = b.readline().rstrip()
        while 0 < len(line):
            if line in a_dict:
                a_dict.pop(line)
            line = b.readline().rstrip()

for element in a_dict:
    print(element)
