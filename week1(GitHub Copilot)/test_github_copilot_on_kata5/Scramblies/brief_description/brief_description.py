def scramble(str1, str2):
    # Create a frequency dictionary for str1
    freq_dict = {}
    for char in str1:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    # Check if str2 can be formed using characters from str1
    for char in str2:
        if char not in freq_dict or freq_dict[char] == 0:
            return False
        freq_dict[char] -= 1
    
    return True