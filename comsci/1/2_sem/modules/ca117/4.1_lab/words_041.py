#!/usr/bin/env python3

import sys
import string

d = {}
for line in sys.stdin:
    a = line.lower().split()
    for word in a:
        word = word.strip(string.punctuation)
        if word.strip() in d:
            d[word.strip()] += 1
        else:
            d[word.strip()] = 1
for key, value in sorted(d.items()):
    print(key + " :", value)
