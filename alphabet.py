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
height = 1

while True:
    if height * height == all_space:
        break
    height += 1

for i in range(height):
    for j in range(height - i):
        if j == height - 1 - i and i != height - 1:
            for k in range(height - j):
                if k == height - 1 - j:
                    print(chr(letter), end="")
                else:
                    print(chr(letter), end=" ")
                letter += 1
        elif i < height - 1:
            print(" ", end=" ")
    if i == height - 1:
        for k in range(last_layer - (whole_triangle - num)):
            if k == last_layer - (whole_triangle - num) - 1:
                print(chr(letter), end="")
            else:
                print(chr(letter), end=" ")
            letter += 1
    print()
