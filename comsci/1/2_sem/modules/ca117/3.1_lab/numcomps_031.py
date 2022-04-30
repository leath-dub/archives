#!/usr/bin/env python3

import sys

def numcomps(int_arr):
    mulps_3 = [n for n in int_arr if not(n % 3)]
    mulps_4 = [n for n in int_arr if not(n % 4)]
    print("Multiples of 3:", mulps_3)
    print("Multiples of 3 squared:", [(n * n) for n in mulps_3])
    print("Multiples of 4 doubled:", [(n * 2) for n in mulps_4])
    print("Multiples of 3 or 4:", [n for n in int_arr if not(n % 3) or not(n % 4)])
    print("Multiples of 3 and 4:", [n for n in int_arr if not(n % 3) and not(n % 4)])


for n in sys.stdin:
    numcomps(list(range(1, int(n) + 1)))
