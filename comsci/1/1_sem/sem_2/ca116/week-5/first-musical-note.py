#!/usr/bin/env python3

n = input()
notes = "~abcdefg"
i = 0
ni = 0
b = 0
while b != 1:
    if n[ni] == notes[i]:
        b = 1
        print(n[ni])
    elif notes[i] == "g":
        i = 0
        ni += 1
    i += 1
