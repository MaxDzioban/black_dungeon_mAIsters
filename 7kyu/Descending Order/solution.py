def sort_digits_descending(n):
    # Convert the integer to a string to be able to iterate over the digits
    str_n = str(n)
    
    # Use sorted() to sort the digits in descending order
    sorted_digits = sorted(str_n, reverse=True)
    
    # Join the sorted digits back into a string and convert it back to an integer
    sorted_n = int(''.join(sorted_digits))
    
    return sorted_n
