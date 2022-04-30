def count_letters(s) -> int:
    if s == "":
        return 0
    if not(s):
        return 0
    return 1 + count_letters(s[1:])
