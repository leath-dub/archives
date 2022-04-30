#!/usr/bin/env python3

import sys
import string

def main():
    alpha = set(string.ascii_lowercase)
    for line in sys.stdin:
        charset = {ch for ch in set("".join(line.lower().split())) if not(ch in string.punctuation) and not(ch in string.digits)}
        if charset == alpha:
            print("pangram")
        else:
            print(f'missing {"".join(sorted(list(alpha - charset)))}')


if __name__ == "__main__":
    main()
