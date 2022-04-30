#!/usr/bin/env python3

n = int(input())
while n != 0:
    m = int(input())
    if m == 0:
        m = 0
    elif m > n:
        print("higher")
    elif m < n:
        print("lower")
    else:
        print("equal")
    n = m
