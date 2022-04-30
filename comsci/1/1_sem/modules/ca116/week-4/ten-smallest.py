#!/usr/bin/env python3

s = int(input())
i = 0
while i < 9:
   x = int(input())
   if x < s:
      s = x
   i += 1
print(s)
