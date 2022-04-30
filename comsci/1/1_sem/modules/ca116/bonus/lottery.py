#!/usr/bin/env python3

import sys

draw = {
    sys.argv[1]: True,
    sys.argv[2]: True,
    sys.argv[3]: True,
}
ticket = sys.stdin.readline().rstrip().split()
while ticket != []:
    score = 0
    if ticket[0] in draw:
        score += 1
    if ticket[1] in draw:
        score += 1
    if ticket[2] in draw:
        score += 1
    if score == 3:
        print(100)
    elif score == 2:
        print(5)
    elif score == 1:
        print(1)
    else:
        print(0)
    ticket = sys.stdin.readline().rstrip().split()
