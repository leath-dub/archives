#!/usr/bin/env python3

import calendar
import sys

days = ["You were born on a Monday and Monday's child is fair of face.",
        "You were born on a Tuesday and Tuesday's child is full of grace.",
        "You were born on a Wednesday and Wednesday's child is full of woe.",
        "You were born on a Thursday and Thursday's child has far to go.",
        "You were born on a Friday and Friday's child is loving and giving.",
        "You were born on a Saturday and Saturday's child works hard for a living.",
        "You were born on a Sunday and Sunday's child is fair and wise and good in every way."]
for line in sys.stdin:
    [year, month, day] = line.split()[::-1]
    print(days[calendar.weekday(int(year), int(month), int(day))])
