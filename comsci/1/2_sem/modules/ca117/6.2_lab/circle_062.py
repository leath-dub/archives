#!/usr/bin/env python3

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    if (x2 - x1) ** 2 + (y2 - y1) ** 2 < (r1 + r2) ** 2:
        return True
    else:
        return False
