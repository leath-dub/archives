#!/usr/bin/env python3

import sys

def main():
    maxi = ("Name", 200000, "0:0")
    for line in sys.stdin:
        invalid = 0
        data = line.strip().split()
        name = data[-6]
        data = data[data.index(name) + 1:]
        for time in data:
            mins = time.split(":")[0]
            secs = time.split(":")[1]
            if not(mins.isnumeric()) or not(secs.isnumeric()):
                invalid = 1
                break
            tot = int(mins) * 60 + int(secs)
            if tot < maxi[1]:
                maxi = (name, tot, time)
    print(maxi[0] + " :", maxi[2])


if __name__ == "__main__":
    main()
