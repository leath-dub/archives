#!/usr/bin/env python3

# search for char in file, if found, let char = a key in a dictionary
# with its position as its value. Then before searching you must check
# if its in the dictionary and search from that position if that is the
# case
import sys

s = sys.stdin.read()
prev_pos = {}
page_n = 0
s_n = 0
while s_n < len(s):
    if s[s_n] in prev_pos:
        parse = prev_pos[s[s_n]]
        page_n = parse[0]
        line_n = parse[1]
        char_n = parse[2] + 1
    else:
        page_n = 0
        line_n = 0
        char_n = 0
    tag = 0
    while page_n < 10 and tag == 0:
        with open("page-" + str(page_n) + ".txt") as page:
            lines = page.readlines()
            while line_n < len(lines) and tag == 0:
                line = lines[line_n]
                while char_n < len(line) and tag == 0:
                    char = line[char_n]
                    if char == s[s_n]:
                        p = page_n
                        li = line_n
                        c = char_n
                        print(str(p) + " " + str(li) + " " + str(c))
                        prev_pos[s[s_n]] = [page_n, line_n, char_n]
                        tag = 1
                    char_n += 1
                char_n = 0
                line_n += 1
        line_n = 0
        page_n += 1
    s_n += 1
