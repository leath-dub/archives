#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
sum_even = 0
prev = 0
curr = 1
nex = 1
while nex < n:
    nex = curr + prev
    prev = curr
    curr = nex
    if prev % 2 == 0:
        sum_even += prev
print(sum_even)
