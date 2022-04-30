#!/usr/bin/env python3

import sys

def main() -> None:
    for line in sys.stdin:
        line = line.strip().split()
        line = sorted([int(n) for n in line], reverse=True)
        print(sum([n for i, n in enumerate(line) if not(i % 3 == 2)]))


if __name__ == "__main__":
    main()
