#!/usr/bin/env python3

import sys

# The way that this solution works is as follows. We keep a global order based
# on the indices i.e. "dcba" is ordered like [3, 2, 1, 0]. We then set the
# order of the first line and continue if their are duplicate characters
# i.e. "abccd" (c is twice). We update the order only based on the order of
# the characters at the duplicate indices and are finished when we have no
# dupes or have read all the words. Then we print the words based on the order
# in a final pass through the words.

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_d = {_: alpha.index(_) for _ in alpha}
def count_sort(s, WRD_LEN) -> list:
    s = s.casefold()  # ignore case
    count = [0] * 26
    for ch in s:
        count[alpha_d[ch]] += 1
    for i, n in enumerate(count):
        if i != 0:
            count[i] += count[i - 1]
    return_arr = [0] * WRD_LEN
    for i, ch in enumerate(s):
        return_arr[count[alpha_d[ch]] - 1] = i
        count[alpha_d[ch]] -= 1

    # returns array with indices that repr order
    return return_arr

def get_dupes(s) -> list:
    s = s.casefold()
    return [i for i, v in enumerate(s) if s.count(v) > 1]


# We will store order as indices(not the characters)
def main() -> None:

    # init order as first line
    gword = sys.stdin.readline().strip()
    word_len = len(gword)
    order = count_sort(gword, word_len)
    dupes = get_dupes(gword)

    words = [gword] + sys.stdin.readlines()
    
    if dupes:

        for word in words:
            word = word.strip()

            # get dupe string and sort it by char(tup[0])
            char_to_i = [(word[i], i) for i in dupes]
            s = sorted(char_to_i, key=lambda tup: tup[0].lower())

            # update the order based on dupe indices
            j = 0
            for i, v in enumerate(order):
                if v in dupes:
                    order[i] = s[j][1]
                    j += 1

            new_dupes = []
            for i in dupes:
                if word.casefold().count(word[i].lower()) > 1:
                    new_dupes.append(i)
            dupes = new_dupes
    
    for word in words:
        
        # Print word based on order list
        for i in order:
            sys.stdout.write(word[i])
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
