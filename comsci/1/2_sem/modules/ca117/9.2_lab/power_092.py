def power(n, m) -> int:
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * power(n, m - 1)
