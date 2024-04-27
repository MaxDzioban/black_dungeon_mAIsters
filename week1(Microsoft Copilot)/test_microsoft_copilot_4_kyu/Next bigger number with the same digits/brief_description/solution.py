def next_bigger(n):
    # Convert the number to a list of digits
    digits = [int(d) for d in str(n)]
    
    # Traverse the list of digits in reverse order
    for i in range(len(digits)-2, -1, -1):
        # If the current digit is less than the next digit
        if digits[i] < digits[i+1]:
            # Find the smallest digit in the tail that is greater than the current digit
            min_larger_index = i + 1 + min(range(len(digits[i+1:])), key=lambda j: digits[i+1:][j] if digits[i+1:][j] > digits[i] else float('inf'))
            # Swap the current digit and the next digit
            digits[i], digits[min_larger_index] = digits[min_larger_index], digits[i]
            # Sort the tail in ascending order
            digits[i+1:] = sorted(digits[i+1:])
            # Convert the list of digits back to a number and return it
            return int(''.join(map(str, digits)))
    
    # If the digits can't be rearranged to form a bigger number, return -1
    return -1
