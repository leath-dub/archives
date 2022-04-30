#!/usr/bin/env python3

import sys

def space(fvar, index, longest):
    if index == 1:  # for clubs
        sys.stdout.write(f'{fvar:<{longest}s}')
    elif index == 2:
        sys.stdout.write(f'{fvar:>2s}')
    else:
        sys.stdout.write(f'{fvar:>3s}')
    if index != 9:
        sys.stdout.write(" ")


stdin = []
longest = 0
for line in sys.stdin:
    line = line.split()
    stdin.append(line)
    # [1:-8] get the name of club(could be multiple words)
    club = " ".join(line[1:-8])
    if len(club) > longest:
        longest = len(club)

titles = ["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]
for i, title in enumerate(titles):
    space(title, i, longest)
sys.stdout.write("\n")

for line in stdin:
    club = " ".join(line[1:-8])
    # Joins line together removing club(gets inserted later)
    arr = "".join(" ".join(line).split(club)).split()
    arr.insert(1, club)
    for i, data in enumerate(arr):
        space(data, i, longest)
    sys.stdout.write("\n")
