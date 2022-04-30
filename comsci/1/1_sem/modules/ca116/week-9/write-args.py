#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
writables = sys.argv[2:]
with open(file_name, "w") as o:
    i = 0
    while i < len(writables):
        o.write(writables[i] + "\n")
        i += 1
