#!/usr/bin/env python3

import sys

def main():
    score_to_name = {}
    sort_index = []
    disqualified = []
    for line in sys.stdin:
        name = " ".join(line.split()[:-3])
        nums = line.split()[-3:]
        invalid = 0
        for ch in nums:
            if not(ch.isnumeric()) or int(ch) < 1:
                invalid = 1
        if invalid == 0:
            nums = [int(n) for n in nums]
        if not(invalid):
            sort_index.append(sum(nums))
            score_to_name[sum(nums)] = name
        else:
            disqualified.append(name)
    sort_index = sorted(sort_index)
    for n in sort_index:
        print(f'{score_to_name[n]}: {n}')
    if len(disqualified):
        disqualified = ", ".join(disqualified)
        print(f'Disqualified: {disqualified}')


if __name__ == "__main__":
    main()
