def create_table(n: int, m: int) -> list[list]:
    '''
    returns list with fibonacci numbers.

    >>> create_table(4, 6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    '''
    if n > 1 and m > 1:
        for i, _ in enumerate(range(m)):
            if i > 0:
                table[0] += [table[0][i - 1] + create_table(n-1, m)[-1][i]]
            else:
                table = [[1]]
        return create_table(n-1, m) + table
    if n <= 1 or m <= 1:
        return [[1 for _ in range(m)] for _ in range(n)]
