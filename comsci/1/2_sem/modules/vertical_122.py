#!/usr/bin/env python3

import sys

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_d = {_: alpha.index(_) for _ in alpha}

# Count sort adjusted to return order of indices
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
    return return_arr  # returns array with indices that rep order


def sort_to_indices(s) -> list:
    len_iter = range(len(s))
    return sorted(len_iter, key=lambda i: s[i].lower())


def get_dupes(s) -> list:
    s = s.casefold()
    return [i for i, v in enumerate(s) if s.count(v) > 1]


# We will store order as indices(not the characters)
def main() -> None:
    store_words = []

    # init order as first line
    gword = sys.stdin.readline().strip()
    # word_len = len(gword)
    store_words.append(gword)
    # order = count_sort(gword, word_len)
    order = sort_to_indices(gword)
    dupes = get_dupes(gword)

    for word in sys.stdin:
        word = word.strip()

        # keep the words for second pass
        store_words.append(word)

        # get dupe indices and sort them via their value
        sorted_dupes = sorted(
                [(word[i], i) for i in dupes],  # e.g ("A", 1)
                key=lambda tup: tup[0].lower())

        dup_iter = 0
        for i, j in enumerate(order):

            # if j in dupes, try update its order
            if j in dupes:
                order[i] = sorted_dupes[dup_iter][1]
                dup_iter += 1

        new_dupes = []
        for i in dupes:

            all_lower = word.casefold()
            ch_lower = word[i].lower()

            if all_lower.count(ch_lower) > 1:
                new_dupes.append(i)

        dupes = new_dupes

    for word in store_words:

        for i in order:
            sys.stdout.write(word[i])
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
