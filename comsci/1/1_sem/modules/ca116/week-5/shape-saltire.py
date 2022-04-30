#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
    if i < n // 2:
        print(i * " " + "*" + (n - (i * 2) - 2) * " " + "*")
        j = i
    elif i == n // 2:
        print(i * " " + "*")
    else:
        print(j * " " + "*" + (n - (j * 2) - 2) * " " + "*")
        j -= 1
    i += 1
