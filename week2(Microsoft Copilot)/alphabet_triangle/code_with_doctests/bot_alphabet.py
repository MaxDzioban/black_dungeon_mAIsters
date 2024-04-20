def print_triangle():
    num = int(input())
    whole_triangle = 0
    last_layer = 0
    letter = ord('A')

    while num > whole_triangle:
        last_layer += 1
        whole_triangle += last_layer

    all_space = whole_triangle * 2 - last_layer
    height = int((all_space ** 0.5) + 0.5)

    for i in range(height):
        for _ in range(height - i):
            if _ == height - 1 - i and i != height - 1:
                for k in range(height - _):
                    print(chr(letter), end=" " if k != height - 1 - _ else "")
                    letter += 1
            elif i < height - 1:
                print(" ", end=" ")
        if i == height - 1:
            for k in range(last_layer - (whole_triangle - num)):
                print(chr(letter), end=" " if k != last_layer - (whole_triangle - num) - 1 else "")
                letter += 1
        print()


if __name__ == "__main__":
    print_triangle()