#!/usr/bin/env python3

i = int(input())
o1 = i % 100
o2 = o1 % 10
g = (i - o1) // 100
e = (o1 - o2) // 10
print(g)
print(e)
print(o2)
