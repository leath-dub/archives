#!/usr/bin/env python3

import sys

for line in sys.stdin:
    prefix = line.split("@")[0]
    sys.stdout.write(prefix[0].capitalize())
    for i, ch in enumerate(prefix):
        if i > 0:
            if ch == ".":
                sys.stdout.write(" ")
                sys.stdout.write(prefix[i + 1].capitalize())
            elif prefix[i - 1] != "." and ch.isdigit() is False:
                sys.stdout.write(ch)
    print()
