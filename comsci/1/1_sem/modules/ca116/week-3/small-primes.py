#!/usr/bin/env python3

n = int(input())

if n == 1:
    print("not prime")
elif n % 2 == 0 and n != 2:
    print("not prime")
elif n % 3 == 0 and n != 3:
    print("not prime")
elif n % 5 == 0 and n != 5:
    print("not prime")
elif n % 7 == 0 and n != 7:
    print("not prime")
else:
    print("prime")
