#!/usr/bin/env python3

from sys import argv

a = []
s = "," + input() + ","
while s != ",end,":
    a.append(s)
    s = "," + input() + ","

arg = argv[1]
i = 0
while i < len(arg):
    if arg[i] == "=":
        head = arg[:i]
        fie = arg[i + 1:]
    i += 1
hlst = ["LatD", "LatM", "Lats", "NS", "LonD", "LonM", "LonS", "EW", "City"]
hindex = 0
i = 0
if head == "State":
    hindex = 9
else:
    while i < len(hlst):
        if hlst[i] == head:
            hindex = i
        i += 1
i = 0
output = []
while i < len(a):
    tmp = a[i]
    commas = 0
    j = 0
    old = 0
    while commas < hindex + 2:
        if tmp[j] == ",":
            commas += 1
            if tmp[old + 1:j] == fie:
                output.append(tmp)
            old = j
        j += 1
    i += 1
i = 0
while i < len(output):
    tmp = output[i]
    print(tmp[1:len(tmp) - 1])
    i += 1
