#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
tag = 0
while i < len(a):
    if tag == 0 and a[i] > "":
        tag += 1
        print(a[i])
    i += 1
