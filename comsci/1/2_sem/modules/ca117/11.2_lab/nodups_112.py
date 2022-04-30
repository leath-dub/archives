#!/usr/bin/env python3

import sys
from string import punctuation

def main() -> None:
    dupes = {}
    for line in sys.stdin:
        line = line.split()
        f = len(line) - 1
        for i, w in enumerate(line):
            wc = w.strip(punctuation).lower()
            if wc not in dupes:
                dupes[wc] = True
                sys.stdout.write(w)
            else:
                sys.stdout.write(".")
            if not(i == f):
                sys.stdout.write(" ")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
