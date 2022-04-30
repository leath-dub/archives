#!/usr/bin/env python3

import sys

vs = "aeiou"

def main() -> None:
    for s in sys.stdin:
        for v in vs:
            nv = (v + "p" + v)
            s = s.replace(nv, v)
        sys.stdout.write(s)


if __name__ == "__main__":
    main()
