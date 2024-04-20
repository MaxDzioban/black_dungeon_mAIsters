import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import memory_usage


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

    def test_memory():
        memory_human = []
        memory_github = []
        input_values = [i for i in range(2, 20000, 500)]  # Example input values to test

        for num in input_values:
            mem = memory_usage((main_human, (num,), {}))
            memory_human.append(mem[-1])

            mem = memory_usage((main_github, (num,), {}))
            memory_github.append(mem[-1])

        print(memory_human)

        print(memory_github)

        plt.plot(input_values, memory_human, color = 'red', label = 'human')
        plt.plot(input_values, memory_github, color = 'blue', label = 'bot')
        
        plt.title('Memory Usage vs. Input Value')
        plt.xlabel('Input Value')
        plt.ylabel('Memory Usage (MB)')
        plt.show()

        plt.legend()

    test_memory()


# def your_function(input_value):
#     # Your function code here
#     # Make sure it performs some memory-intensive operations
#     # For demonstration purposes, let's create a large list
#     data = [i for i in range(input_value)]
#     return data

# # Different input values
# input_values = [1000, 2000, 3000, 4000, 5000]

# # Memory usage container for each input value
# mem_usages = []

# # Measure memory usage for each input value
# for value in input_values:
#     mem_usage = memory_usage((your_function, (value,), {}))
#     mem_usages.append(mem_usage[-1])  # Take the maximum memory usage from the list

# # Plot the results
# plt.plot(input_values, mem_usages, marker='o')
# plt.title('Memory Usage vs. Input Value')
# plt.xlabel('Input Value')
# plt.ylabel('Memory Usage (MB)')
# plt.grid(True)
# plt.show()