#!/usr/bin/env python3

import re
import sys

def sum_factors(n):
    if n == 1:
        return 0
    result = 0
    for num in range(2, n // 2 + 1):
        try:
            if n % num == 0:
                result += num
        except ValueError:
            pass
    return result + 1


def main():
    for n in sys.stdin:
        print(int(n.strip()) == sum_factors(int(n)))


if __name__ == "__main__":
    main()
