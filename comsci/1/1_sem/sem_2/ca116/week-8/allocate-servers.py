#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()
i = 0
cpu = 0
while i < len(a):
    j = i
    counter = 0
    while j < len(a) and not(a[i] + 1000 < a[j]):
        j += 1
        counter += 1
    if counter > cpu:
        cpu = counter
    i += 1
print(cpu)
