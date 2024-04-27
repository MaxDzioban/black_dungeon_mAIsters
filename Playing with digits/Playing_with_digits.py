def dig_pow(n, p):
    # Convert the number into a string
    str_n = str(n)
    total_sum = 0

    # Calculate the sum of digits raised to successive powers
    for i, digit in enumerate(str_n):
        total_sum += int(digit) ** (p + i)

    # Check if there exists a positive integer k
    if total_sum % n == 0:
        return total_sum // n
    else:
        return -1
