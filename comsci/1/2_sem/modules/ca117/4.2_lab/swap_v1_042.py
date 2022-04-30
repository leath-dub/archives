#!/usr/bin/env python3

def swap_keys_values(d):
    return dict({(tup[1], tup[0]) for tup in d.items()})
