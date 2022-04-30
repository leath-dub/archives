#!/usr/bin/env python3

import sys

longest = 0
inp = sys.stdin.readlines()
# find the longest
for line in inp:
    if len(line) > longest:
        longest = len(line)
for line in inp:
    line = line.rstrip()
    print(f'{line:^{longest - 1}}')
