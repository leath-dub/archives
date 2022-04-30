#!/usr/bin/env python3

import sys

vowels = "aeiou"

def main() -> None:
    mx = [0, ""]
    for w in sys.stdin:
        count = 0
        for v in vowels:
            count += w.count(v * 2)
        if mx[0] < count:
            (mx[0], mx[1]) = (count, w.strip())
    print(mx[1])


if __name__ == "__main__":
    main()
