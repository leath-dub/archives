#!/usr/bin/env python3

i = 0
t = 0
while i < 10:
    x = int(input())
    t += x
    t *= 10
    i += 1
t //= 10
j = 0
t2 = 1
while j < 10:
    t2 *= 10
    print(t % t2 // (t2 // 10))
    j += 1
