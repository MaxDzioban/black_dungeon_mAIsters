import matplotlib.pyplot as plt
import time

def create_table(n: int, m: int) -> list[list]:
    '''
    returns list with fibonacci numbers.

    >>> create_table(4, 6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    '''
    if n > 1 and m > 1:
        # print(f'n: {n}, m: {m}')
        for i, _ in enumerate(range(m)):
            if i > 0:
                table[0] += [table[0][i - 1] + create_table(n-1, m)[-1][i]]
            else:
                table = [[1]]
        return create_table(n-1, m) + table
    if n <= 1 or m <= 1:
        return [[1 for _ in range(m)] for _ in range(n)]

def create_table_cop(n: int, m: int) -> list[list]:
    '''
    returns list with fibonacci numbers.

    >>> create_table(4, 6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    '''
    if n <= 1 or m <= 1:
        return [[1 for _ in range(m)] for _ in range(n)]
    
    table = [[1]]
    for i in range(1, m):
        table[0].append(table[0][i - 1] + create_table_cop(n-1, m)[-1][i])
    
    return create_table_cop(n-1, m) + table




lst_1, lst_2 = [], []
for ind in range(0, 10, 1):
    
    print(ind)
    
    t_s_0 = time.time()
    create_table(ind, ind)
    t_e_0 = time.time()

    t_s_1 = time.time()
    create_table_cop(ind, ind)
    t_e_1 = time.time()
    lst_1.append(t_e_0-t_s_0)
    lst_2.append(t_e_1-t_s_1)

plt.plot(range(0, 10), lst_1, label = 'human')
plt.plot(range(0, 10), lst_2, label = 'bot')

plt.xlabel('Input Value')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Input Value')
plt.legend()
plt.show()
