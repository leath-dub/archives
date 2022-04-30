#!/usr/bin/env python3

import sys

def main() -> None:
    odd = []
    for i, w in enumerate(sys.stdin):
        if not(i % 2):
            sys.stdout.write(w)
        else:
            odd.append(w)
    for w in odd[::-1]:
        sys.stdout.write(w)


if __name__ == "__main__":
    main()
