#!/usr/bin/env python3

store = ""
tmp = ""
s = input()
while s != "end":
    i = 0
    while i < len(s.split(".")) - 1:
        tmp = store + " " + s.split(".")[i]
        print(" ".join(tmp.split()) + ".")
        store = ""
        i += 1
    store = store + " " + s.split(".").pop()
    s = input()
