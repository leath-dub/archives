#!/usr/bin/env python3

def swap_unique_keys_values(d):
    new_d = {}
    dups = set({})
    for tup in d.items():
        if not(tup[1] in new_d):
            new_d[tup[1]] = tup[0]
        else:
            dups.add(tup[1])
    return dict({s for s in new_d.items() if s[0] not in dups})
