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