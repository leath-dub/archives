#!/usr/bin/env python3

s = input()
a = s.split()
i = 0
n = int(a[0])
steps = 0
while n != 1:
    if n % 2 == 1:
        n += 1
    n //= 2
    steps += 1
if int(a[1]) >= steps:
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")
