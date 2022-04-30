#!/usr/bin/env python3

import sys

def binf(toFind, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < toFind:
            low = mid + 1
        elif sorted_list[mid] > toFind:
            high = mid - 1
        else:
            return True
    return False


words = [word.strip() for word in sys.stdin if len(word.strip()) > 4]
words_reverse = [word[-1::-1] for word in words]
words = [word.lower() for word in words]
print([word[-1::-1] for word in words_reverse if binf(word.lower(), words)])
