#!/usr/bin/env python3

import sys

def main():
    cards = input().strip().split()
    rank = "A23456789TJQK"
    n_rank = 13 * [0]
    for pair in cards:
        n_rank[rank.index(pair[0])] += 1
    print(max(n_rank))


if __name__ == "__main__":
    main()
