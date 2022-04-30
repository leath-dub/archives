#!/usr/bin/env python3

a_dict = {}
intersect = False

with open("a.txt") as a:
    with open("b.txt") as b:

        line = a.readline().rstrip()
        while 0 < len(line):
            a_dict[line] = None
            line = a.readline().rstrip()

        line = b.readline().rstrip()
        while 0 < len(line):
            if line in a_dict:
                intersect = True
            line = b.readline().rstrip()
if intersect == True:
    print("intersecting")
else:
    print("disjoint")
