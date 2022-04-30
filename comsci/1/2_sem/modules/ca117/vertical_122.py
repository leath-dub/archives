#!/usr/bin/env python3

import sys

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
    store_words.append(gword)
    order = sort_to_indices(gword)
    dupes = get_dupes(gword)

    for word in sys.stdin:
        word = word.strip()
        store_words.append(word)

        if dupes:
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
        for col in order:
            sys.stdout.write(word[col])
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
