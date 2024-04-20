'''Incorrect solution here'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def statement1(s):
    # Check if s is the sum of two primes
    for i in range(2, s):
        if is_prime(i) and is_prime(s - i):
            return False
    return True

def statement2(p):
    # Check if p is the product of two numbers whose sum could not be the sum of two primes
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0 and statement1(i + p//i):
            return False
    return True

def statement3(s):
    # Check if s is the sum of two numbers whose product could be known by Patricia
    for i in range(2, s//2 + 1):
        if statement2(i * (s - i)):
            return False
    return True

def is_solution(a, b):
    return statement1(a + b) and statement2(a * b) and statement3(a + b)
