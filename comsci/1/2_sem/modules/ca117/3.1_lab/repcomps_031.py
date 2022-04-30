#!/usr/bin/env python3

import sys

def numcomps(int_arr):
    mulps_3X = [n if n % 3 else str(n).replace(str(n), "X") for n in int_arr]
    print("Multiples of 3 replaced:", mulps_3X)


for n in sys.stdin:
    numcomps(list(range(1, int(n) + 1)))
