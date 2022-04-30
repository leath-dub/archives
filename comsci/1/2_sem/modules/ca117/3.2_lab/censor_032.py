#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as FILE:
    censored = [line.strip() for line in FILE.readlines()]
text = sys.stdin.read()
text_lower = text.lower()
for word in censored:
    text_lower = text_lower.replace(word, len(word) * "@")
new_text = ""
for i, ch in enumerate(text_lower):
    if ch == "@":
        new_text += "@"
    else:
        new_text += text[i]
sys.stdout.write(new_text)
