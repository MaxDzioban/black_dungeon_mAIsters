def create_table(n, m):
    """
    Create a table with dimensions n and m.
    
    Parameters:
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list[list]: A table of size n x m.
    """
    if n <= 1 or m <= 1:
        return [[1 for _ in range(m)] for _ in range(n)]
    else:
        table = create_table(n - 1, m)
        new_row = [1]
        for i in range(1, m):
            new_row.append(new_row[i - 1] + table[-1][i])
        table.append(new_row)
        return table
