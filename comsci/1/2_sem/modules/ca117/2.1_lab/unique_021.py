#!/usr/bin/env python3

import sys

d = {}
for word in sys.stdin.read().split():
    word = "".join([ch for ch in word if ch.isalpha() or ch.isnumeric()]).lower()
    if word != "" and word not in d:
        d[word] = True
print(len(d))
