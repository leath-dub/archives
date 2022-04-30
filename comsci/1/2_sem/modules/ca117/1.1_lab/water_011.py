#!/usr/bin/env python3

n = int(input())
buckets = [int(i) for i in input().split()]
i = 0
while n - buckets[i] >= 0 and i < len(buckets) - 1:
    n -= buckets[i]
    i += 1
if n - buckets[i] >= 0:
    i += 1
print(i)
