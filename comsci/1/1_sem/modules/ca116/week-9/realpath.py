#!/usr/bin/env python3

from sys import argv

args = argv[1:]
index = 0
while index < len(args):
    arg = args[index]
    root = 0
    if arg[0][0] == "/":
        root = 1
    arg = arg.split("/")
    stack = []
    path = ""
    i = 0
    while i < len(arg):
        if arg[i] == ".." and len(stack) > 0:
            stack.pop()
        elif arg[i] != "." and arg[i] != "..":
            stack.append(arg[i])
        i += 1
    i = 0
    while i < len(stack):
        if stack[i] != "":
            path += stack[i] + "/"
        i += 1
    if root == 1:
        path = "/" + path
    if len(path) > 1:
        path = path[:len(path) - 1]
    print(path)
    index += 1
