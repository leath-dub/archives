#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        s = ""
        for ch in line:
            if ch.isupper():
                s += ch
            else:
                s += "-"
        print(max(s.split("-"), key=len))


if __name__ == "__main__":
    main()
