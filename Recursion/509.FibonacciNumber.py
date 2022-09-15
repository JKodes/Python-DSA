def fib( n: int):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)



if __name__ == '__main__':
   print(fib(n = 4))
