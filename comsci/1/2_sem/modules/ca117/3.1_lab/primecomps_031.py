#!/usr/bin/env python3

import sys 
def isprime(n):
    return len([m for m in list(range(2, n + 1)) if n % m]) == n - 2


def numcomps(int_arr):
    print("Primes:", [n for n in int_arr if isprime(n)])


for n in sys.stdin:
    numcomps(list(range(1, int(n) + 1)))
