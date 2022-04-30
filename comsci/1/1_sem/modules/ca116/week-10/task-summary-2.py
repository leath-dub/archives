#!/usr/bin/env python3

import sys

usr_to_file = {}
score = {}

line = sys.stdin.readline().rstrip()
while 0 < len(line):
    state = line.split(".")[2]
    file = line.split(".")[:2]
    file = ".".join(file)
    usr_to_file[file] = state
    line = sys.stdin.readline().rstrip()
for usr in usr_to_file:
    user = usr.split("/")[0]
    if user not in score:
        score[user] = 0
    if usr_to_file[usr] == "correct":
        score[user] += 1
for item in score:
    print(item + " " + str(score[item]))
