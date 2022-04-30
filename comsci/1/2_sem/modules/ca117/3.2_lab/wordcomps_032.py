#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]
print("Shortest word containing all vowels:", min([word for word in words if sorted(set([ch for ch in word.lower() if ch in "aeiou"])) == list("aeiou")], key=len))
print("Words ending in iary:", len([word for word in words if word.endswith("iary")]))
larg = [""]
for word in words:
    if word.lower().count("e") > larg[0].lower().count("e"):
        larg = [word]
    elif word.lower().count("e") == larg[0].lower().count("e"):
        larg.append(word)
print("Words with most e's:", larg)
