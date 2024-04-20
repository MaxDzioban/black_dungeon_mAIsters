import matplotlib.pyplot as plt
import time
import random
import os
import psutil

# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss
 
# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
 
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))
 
        return result
    return wrapper


def get_tangent(f: callable, x_0: int) -> str:
    """
    
    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
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

def get_tangent_cop(f: callable, x_0: int) -> str:
    """
    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    epsilon = 0.001
    output = []
    for i in range(324):
        h = 10 ** -i
        slope = (f(x_0 + h) - f(x_0)) / h
        output.append(slope)
        if i != 0 and abs(output[i] - output[i-1]) < epsilon:
            b = f(x_0) - x_0 * round(output[i], 2)
            if round(output[i], 2) < 0 < b:
                return f'- {abs(round(output[i], 2))} * x + {b}'
            if round(output[i], 2) > 0 > b:
                return f'{round(output[i], 2)} * x {str(b)[0]} {abs(b)}'
            return f'{round(output[i], 2)} * x - {b}'
        
def generate_random_polynomial(degree: int) -> callable:
    """
    Generate a random polynomial of the given degree and return it as a lambda function.

    Args:
    - degree: The degree of the polynomial.

    Returns:
    - A lambda function representing the random polynomial.

    Example:
    >>> generate_random_polynomial(3)
    lambda x: 2*x**3 + 5*x**2 - 3*x + 1
    """
    coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]
    polynomial = lambda x: sum(coefficients[i] * x**i for i in range(degree + 1))
    return polynomial

@profile
def test():
    lst_1, lst_2 = [], []
    for ind in range(0, 100, 1):
        lst_3, lst_4 = [], []
        for _ in range(0, 50):
            pol = generate_random_polynomial(ind)
            num = random.randint(-200, 200)
            
            t_s_0 = time.time()
            get_tangent(pol, num)
            t_e_0 = time.time()

            t_s_1 = time.time()
            get_tangent_cop(pol, num)
            t_e_1 = time.time()
            lst_3.append(t_e_0-t_s_0)
            lst_4.append(t_e_1-t_s_1)
        lst_1.append(sum(lst_3)/20)
        lst_2.append(sum(lst_4)/20)

    res_1 = sum(lst_1)/100
    res_2 = sum(lst_2)/100

    print(f'The mean result of human code: {res_1} in seconds')
    print(f'The mean result of GitHub Copilot code: {res_2} in seconds')
    print(f'{"Human code is faster" if res_1 < res_2 else "GitHub Copilot code is faster"} by {(res_2/res_1-1)*100 if res_1 < res_2 else (res_1/res_2-1)*100} %')



    plt.plot(range(0, 100), lst_1, label = 'human')
    plt.plot(range(0, 100), lst_2, label = 'bot')

    plt.xlabel('Input Value')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Input Value')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    test()
