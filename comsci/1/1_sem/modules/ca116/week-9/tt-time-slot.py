#!/usr/bin/env python3

start = ""
end = 0
s = input()
while s != "end":
    start = str(int(s.split()[1])) + ":00"
    end = str(int(s.split()[2]) + int(s.split()[1]) - 1) + ":50"
    print(s.split()[0], start, end, " ".join(s.split()[3:]))
    s = input()
