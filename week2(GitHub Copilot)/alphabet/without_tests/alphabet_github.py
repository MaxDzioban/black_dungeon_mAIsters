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

    height = int((2 * whole_triangle - last_layer) ** 0.5)

    for i in range(height):
        if i == height - 1:
            for k in range(last_layer - (whole_triangle - num)):
                if k == last_layer - (whole_triangle - num) - 1:
                    print(chr(letter), end="")
                else:
                    print(chr(letter), end=" ")
                letter += 1
        else:
            for j in range(height - i):
                if j == height - 1 - i:
                    print(chr(letter), end="")
                else:
                    print(chr(letter), end=" ")
                letter += 1
        print()

if __name__ == "__main__":
    main()
