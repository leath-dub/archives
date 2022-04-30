#!/usr/bin/env python3

n = int(input())
prices = input().split()
prices = [int(i) for i in prices]
disc = 0
i = 0
while i < len(prices):
    j = i
    while j < len(prices):
        if prices[j] > prices[i]:
            tmp = prices[i]
            prices[i] = prices[j]
            prices[j] = tmp
        j += 1
    if i % 3 == 2:
        disc += prices[i]
    i += 1
print(disc)
