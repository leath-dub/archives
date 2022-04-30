#!/usr/bin/env python3

import sys

co_ords = sys.stdin.readlines()

top = co_ords[0].rstrip().split()
middle = co_ords[1].rstrip().split()
bottom = co_ords[2].rstrip().split()

mid_points = {}

i = 0
while i < len(middle):
    mid_points[float(middle[i])] = True
    i += 1

straight_lines = 0
i = 0
while i < len(top):
    top_point = float(top[i])
    j = 0
    while j < len(bottom):
        bottom_point = float(bottom[j])
        compare = top_point + (bottom_point - top_point) / 2
        if compare in mid_points:
            straight_lines += 1
        j += 1
    i += 1
print(straight_lines)
