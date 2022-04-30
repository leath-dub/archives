#!/usr/bin/env python3

import sys

files = {
    0: "page-0.txt",
    1: "page-1.txt",
    2: "page-2.txt",
    3: "page-3.txt",
    4: "page-4.txt",
    5: "page-5.txt",
    6: "page-6.txt",
    7: "page-7.txt",
    8: "page-8.txt",
    9: "page-9.txt",
}
inp = sys.stdin.readline()
inp = inp.split()
s = ""
while inp != []:
    file = files[int(inp[0])]
    with open(file) as f_op:
        lines = []
        lines.append(f_op.readline())
        i = 0
        while i < int(inp[1]):
            i += 1
            lines.append(f_op.readline())
        line = lines[len(lines) - 1]
        s += line[int(inp[2])]
    inp = sys.stdin.readline()
    inp = inp.split()
sys.stdout.write(s)
