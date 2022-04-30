#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        (x, y) = line.strip().split()
        x = int(x) > 0
        y = int(y) > 0
        if x and y:
            print("1")
        elif x and not(y):
            print("2")
        elif not(x) and y:
            print("4")
        else:
            print("3")


if __name__ == "__main__":
    main()
