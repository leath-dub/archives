#!/usr/bin/env python3

import sys
for i in sys.stdin:
    if len(i) > 2:
        print(i[0].capitalize() + i[1:-2] + i[-2].capitalize())
