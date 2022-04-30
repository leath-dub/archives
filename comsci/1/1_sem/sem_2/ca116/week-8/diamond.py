#!/usr/bin/env python3

from sys import argv

n = int(argv[1])
spaces = n // 2
astrix = 1
i = 0
while i < n // 2 + 1:
    print(spaces * " " + astrix * "*")
    astrix += 2
    spaces -= 1
    i += 1
astrix -= 4
i = 1
while i < n // 2 + 1:
    print(i * " " + astrix * "*")
    astrix -= 2
    i += 1
