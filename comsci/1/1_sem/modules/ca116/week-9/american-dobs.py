#!/usr/bin/env python3

import sys

file_in = "irish-dobs.txt"
file_out = "american-dobs.txt"
with open(file_in) as inp:
    with open(file_out, "w") as out:
        list_of_lines = inp.readlines() # list
        i = 0
        while i < len(list_of_lines):
            curr_line = list_of_lines[i].split(" ") # string, split to list
            date = curr_line[0].split("/")
            store = date[0]
            date[0] = date[1]
            date[1] = store
            date = "/".join(date)
            curr_line[0] = date
            curr_line = " ".join(curr_line)
            line = line + "\n"
            out.write(curr_line)
            i += 1
