#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]
print("Words containing 17 letters:", [word for word in words if len(word) == 17])
print("Words containing 18+ letters:", [word for word in words if len(word) > 17])
print("Words with 4 a's:", [word for word in words if word.lower().count("a") > 3])
print("Words with 2+ q's:", [word for word in words if word.lower().count("q") > 1])
print("Words containing cie:", [word for word in words if "cie" in word.lower()])
print("Anagrams of angle:", [word for word in words if sorted("angle") == sorted(word.lower()) and word != "angle"])
