#!/usr/bin/env python3

import sys

file_args = sys.argv[1:]
total = 0
i = 0
while i < len(file_args):
    curr_file = file_args[i]
    with open(curr_file) as o:
        lst_of_num = o.readlines()
        j = 0
        while j < len(lst_of_num):
            total += int(lst_of_num[j].rsplit()[0])
            j += 1
    i += 1
print(total)
