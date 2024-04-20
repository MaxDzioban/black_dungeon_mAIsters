import matplotlib.pyplot as plt
import time
import random

def flatten(lst: list) -> list:
    '''
    function that makes one list of items from list of lists
    
    >>> flatten([2, [2, 3, [2, 3]]])
    [2, 2, 3, 2, 3]
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten(3)
    3
    >>> flatten([1, [[[[[]], 4.0], "Hello"], [[3]]], True])
    [1, 4.0, 'Hello', 3, True]
    >>> flatten([[1, [], 4.0], [3]])
    [1, 4.0, 3]
    >>> flatten([[1, [[]]], [3]])
    [1, 3]
    '''
    if lst == [[1, [], 4.0], [3]]:
        pass
    if isinstance(lst, list):
        check_lst = lst[:]
        for i, item in enumerate(lst):
            if isinstance(item, list):
                i = i + len(lst) - len(check_lst)
                if not flatten(item):
                    lst = lst[:i] + lst[i+1:]
                else:
                    lst = lst[:i] + flatten(item) + lst[i+1:]
    return lst

def flatten_cop(lst: list) -> list:
    '''
    function that makes one list of items from list of lists
    
    >>> flatten([2, [2, 3, [2, 3]]])
    [2, 2, 3, 2, 3]
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten(3)
    3
    >>> flatten([1, [[[[[]], 4.0], "Hello"], [[3]]], True])
    [1, 4.0, 'Hello', 3, True]
    >>> flatten([[1, [], 4.0], [3]])
    [1, 4.0, 3]
    >>> flatten([[1, [[]]], [3]])
    [1, 3]
    '''
    if not isinstance(lst, list):
        return lst
    
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_cop(item))
        else:
            result.append(item)
    
    return result

def generate_random_list(depth: int) -> list:
    '''
    Function to generate a random list with nested lists up to a given depth.
    
    Parameters:
    - depth: an integer representing the depth of nested lists
    
    Returns:
    - A randomly generated list with nested lists
    
    Example:
    >>> generate_random_list(3)
    [1, [2, [3, [4]]]]
    '''
    if depth == 0:
        return random.randint(1, 10)
    
    nested_list = []
    for _ in range(random.randint(1, 5)):
        nested_list.append(generate_random_list(depth - 1))
    
    return nested_list


lst_1, lst_2 = [], []
for ind in range(0, 12, 1):
    lst = generate_random_list(ind)
    print(ind)
    
    t_s_0 = time.time()
    flatten(lst)
    t_e_0 = time.time()

    t_s_1 = time.time()
    flatten_cop(lst)
    t_e_1 = time.time()
    lst_1.append(t_e_0-t_s_0)
    lst_2.append(t_e_1-t_s_1)

plt.plot(range(0, 12), lst_1, label = 'human')
plt.plot(range(0, 12), lst_2, label = 'bot')

plt.xlabel('Input Value')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Input Value')
plt.legend()
plt.show()
