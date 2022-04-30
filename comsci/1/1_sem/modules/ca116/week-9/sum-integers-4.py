#!/usr/bin/env python3

import sys

total = 0
files = sys.argv[1:]
i = 0
while i < len(files):
    digits = ""
    file = files[i]
    with open(file) as o:
        s = o.read(1)
        while len(s) > 0:
            if s == "\n" or s == " ":
                total += int(digits)
                digits = ""
            else:
                digits += s
            s = o.read(1)
    i += 1
print(total)
