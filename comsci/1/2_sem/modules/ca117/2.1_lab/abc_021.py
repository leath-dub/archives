#!/usr/bin/env python3

nums = sorted([int(n) for n in input().split()])
order = input()
print(nums["ABC".index(order[0])], nums["ABC".index(order[1])], nums["ABC".index(order[2])])
