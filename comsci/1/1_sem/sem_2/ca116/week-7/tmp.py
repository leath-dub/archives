#!/usr/bin/env python3

from sys import argv



input_lst = []
inp = input()
while inp != "end":
    input_lst.append(inp)
    inp = input()

final = []
index_of_lst = 0
while index_of_lst < len(input_lst):

    pattern = argv[1:]
    pat = pattern[0]
    len_of_pattern = len(pattern[0])
    s = input_lst[index_of_lst]
    i = 0
    compare_string = ""
    while i < len(s) and not(s[i] == pat[0]):
        i += 1
    if i < len(s):
        newstr = s[i:]
        if len(newstr) >= len_of_pattern:
            j = 0
            while j < len_of_pattern:
                compare_string += newstr[j]
                j += 1
            if compare_string == pattern[0]:
                final.append(s)
    index_of_lst += 1
i = 0
while i < len(final):
    print(final[i])
    i += 1
