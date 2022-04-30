#!/usr/bin/env python3

import sys

#for line in sys.stdin:
#    line = "".join([ch.lower() for ch in line.strip() if ch.isalpha() or ch.isnumeric()])
#    print(line[::-1] == line)
test = ["".join([ch.lower() for ch in line.strip() if ch.isalpha() or ch.isnumeric()]) for line in sys.stdin]
test = [print(line[::-1] == line) for line in test]
