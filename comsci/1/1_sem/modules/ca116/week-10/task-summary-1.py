#!/usr/bin/env python3

import sys

task_summary = {}

task = sys.stdin.readline().rstrip()
while 0 < len(task):
    task = task.split(".")
    task_summary[task[0] + "." + task[1]] = task[2]
    task = sys.stdin.readline().rstrip()
for task in task_summary:
    if task_summary[task] == "correct":
        print(task)
