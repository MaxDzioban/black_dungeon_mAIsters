def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    max_dict = {}
    for value in film_keywords.values():
        for i in value:
            max_dict[i] = max_dict.get(i, 0) + 1
    output = sorted(max_dict.items(), key=lambda x: x[1], reverse=True)[:num_of_films]
    return output