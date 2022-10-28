def  fib(n, cache):

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fib(n - 1) + (n - 2)
    return cache[n]


if __name__ == 'main':
    print(fib(5, {}))