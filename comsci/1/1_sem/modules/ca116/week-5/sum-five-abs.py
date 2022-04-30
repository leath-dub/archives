#!/usr/bin/env python3

i = 0
t = 0
while i < 5:
    n = int(input())
    if n < 0:
        t += n
    else:
        n = n * -1
        t += n
    i += 1
print(t * -1)
