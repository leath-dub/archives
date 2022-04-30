#!/usr/bin/env python3

import sys

once = {}

line = sys.stdin.readline().rstrip()
while 0 < len(line):
    if line in once:
        once[line] = False
    else:
        once[line] = True
    line = sys.stdin.readline().rstrip()
for item in once:
    if once[item] is True:
        print(item)
