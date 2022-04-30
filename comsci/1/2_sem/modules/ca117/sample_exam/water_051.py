#!/usr/bin/env python3

def main():
    litres = int(input())
    buckets = [int(n) for n in input().strip().split()]
    end = len(buckets) - 1
    sum_buck = sum(buckets)
    while sum_buck > litres:
        sum_buck -= buckets[end]
        end -= 1
    print(len(buckets[:end + 1]))


if __name__ == "__main__":
    main()
