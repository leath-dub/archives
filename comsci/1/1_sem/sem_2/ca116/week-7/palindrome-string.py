#!/usr/bin/env python3

w = input()
i = 0
rev = ""
while i < len(w):
    rev = w[i] + rev
    i += 1
if rev == w:
    print("palindrome")
