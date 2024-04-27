def stock_list(stocklist, categories):
    category_totals = {category: 0 for category in categories}

    for book in stocklist:
        code, quantity = book.split()
        category_code = code[0]

        if category_code in category_totals:
            category_totals[category_code] += int(quantity)
    if all(value == 0 for value in category_totals.values()):
        return ""
    result = " - ".join(f"({category} : {total})" for category, total in category_totals.items())
    return result
