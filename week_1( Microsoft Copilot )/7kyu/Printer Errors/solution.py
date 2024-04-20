def printer_error(control_string):
    errors = sum(1 for char in control_string if char > 'm')
    return f"{errors}/{len(control_string)}"

# Example usage:
print(printer_error("aaabbbbhaijjjm"))  # Output: "0/14"
