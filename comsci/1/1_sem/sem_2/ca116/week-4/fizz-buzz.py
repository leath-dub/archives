#!/usr/bin/env python3

n = int(input())
i = 0
while i < n + 1:
    if i == 0:
        i = i
    elif i % 3 == 0 and i % 5 == 0:
        print("fizz-buzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
    i += 1
