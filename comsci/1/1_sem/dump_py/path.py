#!/usr/bin/env python3

from sys import argv

args = argv[1:]
arg = "/\n/".join(args)
arg = arg.split("/")
i = 0
while i < len(arg):
    if arg[i] == "":
        arg[i + 1] = "/" + arg[i + 1]
    i += 1
print(arg)
