#!/usr/bin/env python3

w = int(input())
h = int(input())

bmi = w / (h * h) * 10000

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi >= 30:
    print("obese")
else:
    print("overweight")
