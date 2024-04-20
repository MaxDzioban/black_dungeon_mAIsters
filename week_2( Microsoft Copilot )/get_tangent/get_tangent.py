import timeit
import matplotlib.pyplot as plt

# Your original function
def get_tangent_orig(f: callable, x_0: int) -> str:
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

# The provided function
def get_tangent_provided(f: callable, x_0: int) -> str:
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

# Test function
def f(x):
    return x**2

# Measure execution time
orig_times = [timeit.timeit(lambda: get_tangent_orig(f, 1), number=n) for n in range(1, 101)]
provided_times = [timeit.timeit(lambda: get_tangent_provided(f, 1), number=n) for n in range(1, 101)]

# Plot results
plt.plot(range(1, 101), orig_times, label='Original')
plt.plot(range(1, 101), provided_times, label='Provided')
plt.xlabel('Number of Function Calls')
plt.ylabel('Execution Time (s)')
plt.title('Comparison of Execution Time')
plt.legend()
plt.show()
