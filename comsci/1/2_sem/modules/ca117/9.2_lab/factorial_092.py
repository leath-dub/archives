def factorial(n) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return n
    return n * factorial(n - 1)
