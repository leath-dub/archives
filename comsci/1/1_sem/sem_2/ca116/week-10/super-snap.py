#!/usr/bin/env python3

import sys

animals = {}

animal = sys.stdin.readline().rstrip()
while 0 < len(animal) and not(animal in animals):
    if animal not in animals:
        animals[animal] = 1
    animal = sys.stdin.readline().rstrip()

if 0 < len(animal):
    sys.stdout.write("snap: " + animal + "\n")

