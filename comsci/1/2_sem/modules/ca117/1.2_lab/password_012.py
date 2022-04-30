#!/usr/bin/env python3

import sys

for pwd in sys.stdin:
    pwd = pwd.rstrip()
    count = [0, 0, 0, 0]
    for ch in pwd:
        if ch.islower() is True:
            count[0] = 1
        elif ch.isupper() is True:
            count[1] = 1
        elif ch.isdigit() is True:
            count[2] = 1
        else:
            count[3] = 1
    print(sum(count))
