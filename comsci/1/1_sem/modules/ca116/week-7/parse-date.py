#!/usr/bin/env python3

date = input()
i = 0
while date[i] != " ":
    i += 1
day = date[:i]
k = i
while date[i + 1] != " ":
    i += 1
day_of_month = date[k + 1:i + 1]
j = len(date) - 1
while date[j] != " ":
    j -= 1
year = date[j + 1:]
month = date[i + 2:j - 1]
print(month + " " + day_of_month + ", " + year + " (" + day + ")")
