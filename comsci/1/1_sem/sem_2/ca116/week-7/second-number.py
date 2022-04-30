#!/usr/bin/env python3

s = input()
n = len(s)
j = 0
i = 0
while i < len(s) and not("0" <= s[i] and s[i] <= "9"):
    i += 1
if i < len(s):
    j = i + 1
    while j < len(s) and "0" <= s[j] and s[j] <= "9":
        j += 1
s = s[j:]
j = 0
while j < len(s) and not("0" <= s[j] and s[j] <= "9"):
    j += 1
if j < len(s):
    k = j + 1
    while k < len(s) and "0" <= s[k] and s[k] <= "9":
        k += 1
    print(s[j:k], n - len(s) + j)
