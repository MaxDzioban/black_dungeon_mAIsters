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
    if not isinstance(lst, list):
        return lst
    
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    
    return result