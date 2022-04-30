#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
tag = 0
while i < len(a):
    tmp = a[i]
    if tag < 1 and tmp[:len(s)] == s:
        tag += 1
        print(a[i])
    i += 1
