#!/usr/bin/env python3

import sys

def factors(n):
    factors = []
    factors.append(n)
    for m in range(2, n // 2 + 1):
        if n % m == 0:
            factors.append(m)
    return set(factors)


def quad(a, b, c):
    af = factors(abs(a))
    bf = factors(abs(b))
    cf = factors(abs(c))
    inter = af & bf & cf
    if inter:
        a = a / min(inter)
        b = b / min(inter)
        c = c / min(inter)
    discrim = b * b - (4 * a) * c
    if discrim < 0:
        return "None"
    r1 = (-b + (discrim) ** 0.5) / (2 * a)
    r2 = (-b - (discrim) ** 0.5) / (2 * a)
    return (r1, r2)


def main():
    for abc in sys.stdin:
        (a, b, c) = [int(n) for n in abc.strip().split()]
        try:
            (r1, r2) = quad(a, b, c)
            print(f'r1 = {r1}, r2 = {r2}')
        except ValueError:
            print("None")


if __name__ == "__main__":
    main()
