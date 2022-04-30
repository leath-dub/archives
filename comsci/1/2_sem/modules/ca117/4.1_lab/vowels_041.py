#!/usr/bin/env python3

import sys

data = sys.stdin.read().lower()
n_vowels = [
    (len([v for v in data if v == "a"]), "a :"),
    (len([v for v in data if v == "e"]), "e :"),
    (len([v for v in data if v == "i"]), "i :"),
    (len([v for v in data if v == "o"]), "o :"),
    (len([v for v in data if v == "u"]), "u :")
]
n_vowels = sorted(n_vowels, reverse=True)
w = len(str(n_vowels[0][0]))
for tup in n_vowels:
    print(tup[1], f'{tup[0]:{w}}')
