#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

encrypt = {}

i = 0
while i < len(src):
    encrypt[src[i]] = dst[i]
    i += 1

s = sys.stdin.read()
encrypted = ""
i = 0
while i < len(s):
    if s[i] not in encrypt:
        encrypt[s[i]] = s[i]
    encrypted += encrypt[s[i]]
    i += 1
sys.stdout.write(encrypted)
