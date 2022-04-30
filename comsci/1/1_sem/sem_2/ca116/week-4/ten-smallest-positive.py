#!/usr/bin/env python3

smallest = int(input())
i = 0
while i < 9:
    x = int(input())
    if x > 0:
        if x < smallest:
            smallest = x
    i += 1
print(smallest)
