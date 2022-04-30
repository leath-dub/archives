#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        if int(line) < 400:
            print(1)
        else:
            print(int(line) // 400)


if __name__ == "__main__":
    main()
