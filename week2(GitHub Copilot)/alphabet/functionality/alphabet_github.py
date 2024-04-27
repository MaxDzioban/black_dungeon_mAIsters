import math

def main():
    num = int(input())
    whole_triangle = 0
    last_layer = 0
    letter = 65

    while True:
        last_layer += 1
        whole_triangle += last_layer
        if num <= whole_triangle:
            break
        
    all_space = whole_triangle * 2 - last_layer
    height = int(math.sqrt(all_space))

    pattern = [[chr(letter) if j == height - 1 - i and i != height - 1 else " " for j in range(height - i)] for i in range(height)]
    pattern[-1] = [chr(letter) for letter in range(letter, letter + last_layer - (whole_triangle - num) + 1)]

    for row in pattern:
        print(" ".join(row))

if __name__ == "__main__":
    main()