#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
tmp = 0
while i < len(a):
    tmp = a[i]
    if tmp[:len(s)] == s:
        print(a[i])
    i += 1
