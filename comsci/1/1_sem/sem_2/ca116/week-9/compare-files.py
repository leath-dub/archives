#!/usr/bin/env python3

import sys

row = 0
col = 0
res = ""
files = sys.argv[1:]
with open(files[0]) as file_0:
    with open(files[1]) as file_1:
        f0 = file_0.read(1)
        f1 = file_1.read(1)
        while f0 != "" and f1 != "":
            if f0 != f1:
                res = str(row) + " " + str(col - 1)
            elif f0 == "\n":
                row += 1
                col = 0
            f0 = file_0.read(1)
            f1 = file_1.read(1)
            col += 1
        if f0 != "":
            res = str(row) + " " + str(col - 1)
        elif f1 != "":
            res = str(row) + " " + str(col - 1)
if len(res) > 0:
    print(res)
