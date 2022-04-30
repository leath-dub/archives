#!/usr/bin/env python3

import sys

s = sys.stdin.read()
s = s.split("\n\n")
s = "\n".join(s)
s = s.split(" ")
s = "\n".join(s)
sys.stdout.write(s)
