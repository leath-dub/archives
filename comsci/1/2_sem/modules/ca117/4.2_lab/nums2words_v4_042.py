#!/usr/bin/env python3

import sys

pots = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred"
}
numal = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]
def ntow(n):
    if n < 20:
        return numal[n]
    elif n % 10:
        return pots[n - n % 10] + "-" + numal[n % 10]
    else:
        return pots[n]


for line in sys.stdin:
    print(" ".join([ntow(int(s)) for s in line.strip().split()]))
