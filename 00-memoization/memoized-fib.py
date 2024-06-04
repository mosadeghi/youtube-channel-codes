def make_fib():
    values = {0:1, 1:1}
    def fib(n):
        if n not in values:
            values[n] = fib(n-1) + fib(n-2)
        return values[n]
    return fib
fib = make_fib()

if __name__ == "__main__":
    i = 1000
    print(f"fib({i})={fib(i)}")
