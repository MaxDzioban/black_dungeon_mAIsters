import timeit
import matplotlib.pyplot as plt
import psutil
import os
import random
from memory_profiler import memory_usage

def get_tangent_orig(f: callable, x_0: int) -> str:
    '''My get tangent'''
    output = []
    for i in range(324):
        output.append((f(x_0 + 10**-i) - f(x_0)) / (10**-i))
        if i != 0 and abs(output[i] - output[i-1]) < 0.001:
            b = f(x_0) - x_0*round(output[i], 2)
            if round(output[i], 2) < 0 < b:
                return f'- {abs(round(output[i], 2))} * x + {b}'
            if round(output[i], 2) > 0 > b:
                return f'{round(output[i], 2)} * x {str(b)[0]} {abs(b)}'
            return f'{round(output[i], 2)} * x - {b}'

def get_tangent_provided(f: callable, x_0: int) -> str:
    '''Get tangent bot'''
    output = [0]
    for i in range(1, 324):
        h = 10**-i
        f1 = f(x_0 + h)
        f0 = f(x_0)
        output.append((f1 - f0) / h)
        if abs(output[i] - output[i-1]) < 0.001:
            slope = round(output[i], 2)
            b = f0 - x_0*slope
            if slope < 0 < b:
                return f'- {abs(slope)} * x + {b}'
            if slope > 0 > b:
                return f'{slope} * x {str(b)[0]} {abs(b)}'
            return f'{slope} * x - {b}'
    return 'The function did not converge'


def generate_random_polynomial(degree: int) -> callable:
    coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]
    polynomial = lambda x: sum(coefficients[i] * x**i for i in range(degree + 1))
    return polynomial


def memory_test():
    input_values = [generate_random_polynomial(i) for i in range(1, 100, 5)]
    mem_usages_1 = []
    mem_usages_2 = []
    for value in input_values:
        num = random.randint(-100, 100)
        mem_usage = memory_usage((get_tangent_orig, (value,num), {}))
        mem_usages_1.append(mem_usage[-1])
        mem_usage = memory_usage((get_tangent_provided, (value,num), {}))
        mem_usages_2.append(mem_usage[-1])
    plt.plot(range(1,100,5), mem_usages_1, label = 'human')
    plt.plot(range(1,100,5), mem_usages_2, label = 'GitHub Copilot')
    plt.title('Memory Usage vs. Input Value')
    plt.xlabel('Input Value')
    plt.ylabel('Memory Usage (MB)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    memory_test()

