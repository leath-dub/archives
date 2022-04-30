#!/usr/bin/env python3

mark = int(input())
print("first: " + str(mark >= 70))
print("second: " + str(mark >= 50 and mark <= 69))
print("third: " + str(mark >= 40 and mark <= 49))
print("fail: " + str(mark < 40))
