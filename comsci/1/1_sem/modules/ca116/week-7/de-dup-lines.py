#!/usr/bin/env python3

lines = [input()]
out = []
line = lines[0]
out.append(line)
while line != "end":
    tag = 0
    line = input()
    i = 0
    while i < len(lines):
        if line == lines[i]:
            tag = 1
        i += 1
    lines.append(line)
    if tag == 0:
        out.append(line)
i = 0
while i < len(out) - 1:
    print(out[i])
    i += 1
