def fib(f, n):
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10
    return f[n]

def last_fib_digit(n):
    f = [0] * 61
    fib(f, 60)
    return f[n % 60]