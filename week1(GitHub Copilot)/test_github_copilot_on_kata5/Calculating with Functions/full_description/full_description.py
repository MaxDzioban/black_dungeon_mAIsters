def zero(operation=None):
    if operation:
        return operation(0)
    return 0

def one(operation=None):
    if operation:
        return operation(1)
    return 1

def two(operation=None):
    if operation:
        return operation(2)
    return 2

def three(operation=None):
    if operation:
        return operation(3)
    return 3

def four(operation=None):
    if operation:
        return operation(4)
    return 4

def five(operation=None):
    if operation:
        return operation(5)
    return 5

def six(operation=None):
    if operation:
        return operation(6)
    return 6

def seven(operation=None):
    if operation:
        return operation(7)
    return 7

def eight(operation=None):
    if operation:
        return operation(8)
    return 8

def nine(operation=None):
    if operation:
        return operation(9)
    return 9

def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num

# Test cases
print(seven(times(five()))) # Output: 35
print(four(plus(nine()))) # Output: 13
print(eight(minus(three()))) # Output: 5
print(six(divided_by(two()))) # Output: 3
print(eight(divided_by(three()))) # Output: 2