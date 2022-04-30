#!/usr/bin/env python3

from sys import argv

args = argv[1:]
args = "//".join(args)
args = args.split("/")
a = []
prev = args[0]
top = ""
i = 0
while i < len(args):
    curr = args[i]
    if (args[i] == args[1] and args[0] == "") or (args[i] == "" and top == "\n"):
        args[i] = "/" + args[i]
    if args[i] != "." and args[i] != ".." and args[i] != "":
        a.append(args[i])
        top = args[i]
    if args[i] == "" and args[i + 1] == "":
        a.append("\n")
        top = "\n"
    if curr == ".." and top != "/" and top != "\n":
        a.pop()
        top = a[len(a) - 1]
    prev = args[i]
    i += 1
s = ""
print(a)
i = 0
while i < len(a):
    s += a[i]
    i += 1
print(s)
