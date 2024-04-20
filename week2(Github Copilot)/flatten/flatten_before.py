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