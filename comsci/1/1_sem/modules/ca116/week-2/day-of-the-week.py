#!/usr/bin/env python3

n = int(input())
m = int(input())
day_of_year = (n - 1) * 30 + m
print((day_of_year - 1) % 7 + 1)
