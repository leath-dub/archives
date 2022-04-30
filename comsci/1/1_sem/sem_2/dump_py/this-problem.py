#!/usr/bin/env python3

import sys

def sort_max(array):
    array.sort()
    array.reverse()
    return array

def third_of_group():
    all_inp = sys.stdin.read()
    all_inp = all_inp.split("\n")[1]
    array = all_inp.split()
    sum_of_3rd = 0
    for i, value in enumerate(array):
        if int(i) % 3 == 2:
            sum_of_3rd += int(value)
    if sum_of_3rd > 0:
        return sys.stdout.write(str(sum_of_3rd))
third_of_group()
