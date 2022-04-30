#!/usr/bin/env python3

import sys

for i in sys.stdin:
    pair = i.split()
    first = pair[0].lower()
    second = pair[1].lower()
    isTrue = "False"
    for j, val in enumerate(second):
        # find the start character
        if val == first[0] and second[j:j + len(first)] == first:
            isTrue = "True"
    print(isTrue)
