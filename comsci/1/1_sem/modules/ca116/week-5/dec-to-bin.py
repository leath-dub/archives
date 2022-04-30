#!/usr/bin/env python3

deci = int(input())
pwr = 1
log = 0
result = 0
while deci > 0:
    if deci - pwr == 0:
        result += log // 100
    if deci - pwr < 0:
        result += 10 ** (log - 1)
        deci -= pwr // 2
        pwr = 1
        log = 0
    pwr *= 2
    log += 1
print(result)
