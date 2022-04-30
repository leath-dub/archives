#!/usr/bin/env python3

import sys

for i in sys.stdin:
    length = len(i) - 1  # sys.stdin counts '\n' char as part of string
    if length % 2 > 0:
        print(i[length // 2])
    else:
        print("No middle character!")
