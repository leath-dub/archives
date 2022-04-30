#!/usr/bin/env python3

import sys

def add_string(arr, col, ch) -> None:
    if len(arr) - 1 < col:
        arr.append(ch)
    else:
        arr[col] += ch

def main() -> None:
    return_words = list()
    for word in sys.stdin:
        word = word.strip()
        for i, ch in enumerate(word):
            add_string(return_words, i, ch)
    return_words = sorted(return_words, key=lambda w: w.casefold())
    for i in range(len(return_words[0])):
        for word in return_words:
            sys.stdout.write(word[i])
        print("")


if __name__ == "__main__":
    main()
