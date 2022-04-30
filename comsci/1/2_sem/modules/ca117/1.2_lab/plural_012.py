#!/usr/bin/env python3

import sys

def isvowel(ch):
    vowels = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }
    if ch in vowels:
        return True
    else:
        return False


for word in sys.stdin:
    word = word.rstrip()
    case0 = "ch-sh-s-x-z"
    if word[-2] in case0 or word[-1] in case0:
        print(word + "es")
    elif word.endswith("y") and isvowel(word[-2]) is False:
        print(word.rstrip("y") + "ies")
    elif word.endswith("fe"):
        print(word.rstrip("fe") + "ves")
    elif word.endswith("f"):
        print(word.rstrip("f") + "ves")
    elif word.endswith("o"):
        print(word + "es")
    else:
        print(word + "s")
