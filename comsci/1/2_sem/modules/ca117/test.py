#!/usr/bin/env python3

import sys

class Commands(object):

    def __init__(self, commands=["def", "calc", "clear"]):
        self.vars = {}
        self.commands = commands

    def addvar(self, ref, val):
        self.vars[ref] = val

    def clear(self):
        self.__init__()

    def calc(self, a_to_sum):
        total = 0
        for i, arg in enumerate(a_to_sum):
            if (i - 1) % 2:
                try:
                    if a_to_sum[i - 1] == "-":
                        total -= self.vars[arg]
                    else:  # positive
                        total += self.vars[arg]
                except KeyError:  # var not found
                    return "unknown"
        for (k, v) in self.vars.items():
            if v == total:
                return k
        return "unknown"

def main():
    c = Commands()
    for line in sys.stdin:
        line = line.strip().split()
        raw = " ".join(line[1:])
        cmd = line[0]
        match cmd:
            case "def":
                c.addvar(line[1], int(line[2]))
            case "calc":
                print("{} {}".format(raw, c.calc(line[1:])))
            case "clear":
                c.clear()
            default:
                print("'{}' not a command".format(cmd))


if __name__ == "__main__":
    main()
