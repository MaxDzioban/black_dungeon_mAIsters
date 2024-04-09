from collections import Counter

def scramble(str1, str2):
    # Create a Counter object for each string
    counter1 = Counter(str1)
    counter2 = Counter(str2)

    # Check if all characters in str2 are in str1
    for char in counter2:
        if counter2[char] > counter1.get(char, 0):
            return False

    return True
