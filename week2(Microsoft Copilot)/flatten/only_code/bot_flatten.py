def flatten(lst):
    """Flatten a nested list.

    Args:
        lst: A list that may contain nested lists.

    Returns:
        A flattened list.
    """
    if not isinstance(lst, list):
        return lst
    else:
        result = []
        for i in lst:
            if isinstance(i, list):
                result += flatten(i)
            else:
                result.append(i)
        return result
