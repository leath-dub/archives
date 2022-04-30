def fib(n, m):
    print(n)
    if m >= 1000:
        return n
    else:
        return fib(m, n + m)
fib(0, 1)
