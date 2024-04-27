def sort_strings_by_length(arr):
    return sorted(arr, key=len)
strings = ["short", "longer", "longest", "a"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)  # Output: ['a', 'short', 'longer', 'longest']
