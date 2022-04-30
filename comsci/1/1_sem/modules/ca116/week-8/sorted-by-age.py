#!/usr/bin/env python3

len_mnth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = []
name = []
s = input()
while s != "end":
    date.append(s[:8])
    name.append(s[9:])
    s = input()
i = 0
while i < len(date):
    s = date[i]
    k = 0
    total = 0
    while k < int(s[3:5]):
        total += len_mnth[k]
        k += 1
    date[i] = int(s[:2]) + total + int(s[6:8]) * 365
    i += 1
j = 0
while j < len(date):
    i = j
    while i < len(date):
        if date[i] < date[j]:
            tmp = date[i]
            tmp2 = name[i]
            date[i] = date[j]
            name[i] = name[j]
            date[j] = tmp
            name[j] = tmp2
        i += 1
    print(name[j])
    j += 1
