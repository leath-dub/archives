#!/usr/bin/env python3

import sys

for i in sys.stdin:
    if len(i) > 3:
        print(i[1:-2])
