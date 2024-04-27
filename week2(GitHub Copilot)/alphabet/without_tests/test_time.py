def main_human(num):
    # num = int(input())
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
def main_github(num):
    # num = int(input())
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
    # main()
    # print("hi")
    import time
    import matplotlib.pyplot as plt

    def test_execution_time():
        execution_times_human = []
        execution_times_github = []
        input_values = [i for i in range(1, 3000, 25)]  # Example input values to test

        for num in input_values:
            start_time = time.time()
            main_human(num)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times_human.append(execution_time)

            start_time = time.time()
            main_github(num)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times_github.append(execution_time)

        plt.plot(input_values, execution_times_human, color = 'red', label = 'human')
        plt.plot(input_values, execution_times_github, color = 'blue', label = 'bot')
        
        plt.xlabel('Input Value')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time vs Input Value')
        plt.legend()
        plt.show()

    test_execution_time()