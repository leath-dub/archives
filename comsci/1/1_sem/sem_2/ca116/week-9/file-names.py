#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()
i = 0
while i < len(a):
    curr_str = a[i]
    curr_str = a[i].split("/")
    if len(curr_str) > 1:
        sys.stdout.write(curr_str[len(curr_str) - 1])
    else:
        sys.stdout.write(curr_str[0])
    i += 1
