#!/usr/bin/env python3

i = 0
n = int(input())
while i < 5:
    m = int(input())
    if m > n:
        print("higher")
    elif m < n:
        print("lower")
    else:
        print("equal")
    n = m
    i += 1
