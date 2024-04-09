def printer_error(s):
    # Count the number of errors
    error_count = 0
    valid_colors = "abcdefghijklm"

    for color in s:
        if color not in valid_colors:
            error_count += 1

    # Calculate the error rate as a string representing a rational
    error_rate = f"{error_count}/{len(s)}"

    return error_rate