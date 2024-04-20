'''Microsoft Copilot tried something, but was not even close'''
def generate_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if all(i % p > 0 for p in primes):
            primes.append(i)
        i += 1
    return primes

def binary_search(p, query):
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if query(p, m):
            l = m
        else:
            r = m
    return l

def play(query):
    primes = generate_primes(400)  # generate first 400 primes
    factors = []
    for p in primes:
        e = binary_search(p, query)
        if e > 0:
            factors.append(e)
    total_pairs = 1
    for e in factors:
        total_pairs *= (e + 1) ** 2
    total_pairs -= len(factors)  # subtract pairs where gcd(a, b) = 1
    return total_pairs
