'''
Work with given list of films and its keywords
'''
import time
import matplotlib.pyplot as plt
from collections import Counter
from heapq import nlargest
from random import choice, randint
from string import ascii_lowercase
from collections import Counter
from heapq import nlargest
from memory_profiler import memory_usage, profile

def find_film_keywords(film_keywords: dict, film_name: str):
    '''
    Returns set of keywords used in film
    >>> find_film_keywords({'magic' : ['Duck Out (1927)']}, 'Duck Out (1927)')
    {'magic'}
    '''
    return {key for key,value in film_keywords.items() for i in value if film_name == i}

# Original function
def find_films_with_keywords_original(film_keywords: dict, num_of_films: int):
    '''
    Returns tuple with (film name, max_keywords)
    >>> find_films_with_keywords_original({'gonki': ['nfs_mw', 'dark souls'], 'tututu': ['dark souls', \
'fepeen'], 'yabko': ['fepeen', 'dark souls', 'nfs_mw'], 'gegege' : ['abc'], 'hi': ['dark room', \
'nfs_mw', 'abc']}, 4)
    [('dark souls', 3), ('nfs_mw', 3), ('abc', 2), ('fepeen', 2)]
    '''
    output = []
    max_dict = {}
    for value in film_keywords.values():
        for i in value:
            max_dict[i] = max_dict.setdefault(i, 0) + 1
    for i in range(num_of_films):
        for key, value in sorted(max_dict.items()):
            if value == max(max_dict.values()):
                if (key, value) not in output:
                    output.append((key, value))
                    break
        max_dict = {a:b for a,b in max_dict.items() if a != output[i][0]}
    return sorted(output, key = lambda x: x[1], reverse=True)

def find_films_with_keywords_optimized(film_keywords: dict, num_of_films: int):
    """
    This function finds the films with the most keywords.

    Args:
    film_keywords: A dictionary where the keys are keywords and the values are lists of films.
    num_of_films: The number of films with the most keywords to return.

    Returns:
    A list of tuples where each tuple contains a film name and its count of keywords.

    >>> find_films_with_keywords_optimized({'gonki': ['nfs_mw', 'dark souls'], \
    'tututu': ['dark souls', 'fepeen'], 'yabko': ['fepeen', 'dark souls', \
    'nfs_mw'], 'gegege' : ['abc'], 'hi': ['dark room', 'nfs_mw', 'abc']}, 4)
    [('dark souls', 3), ('nfs_mw', 3), ('abc', 2), ('fepeen', 2)]
    """
    film_counts = Counter(film for films in film_keywords.values() for film in films)
    output = sorted(
        film_counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:num_of_films]
    return output


def generate_test_data(num_films, num_keywords):
    '''Generate test data'''
    return {f'film{i}': [choice(ascii_lowercase) for _ in range(randint(1, num_keywords))] for i in range(num_films)}

def test_graph():
    num_films_list = list(range(100, 1100, 100))
    original_times = []
    optimized_times = []

    for num_films in num_films_list:
        test_data = generate_test_data(num_films, 10)

        start_time = time.time()
        find_films_with_keywords_original(test_data, 5)
        original_times.append(time.time() - start_time)

        start_time = time.time()
        find_films_with_keywords_optimized(test_data, 5)
        optimized_times.append(time.time() - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(num_films_list, original_times, label='Original')
    plt.plot(num_films_list, optimized_times, label='Optimized')
    plt.xlabel('Number of films')
    plt.ylabel('Execution time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.title('Comparison of Execution Time')
    plt.show()

def memory_test(data):
    @profile
    def test_my():
        find_films_with_keywords_original(data, 5)

    @profile
    def test_bot():
        find_films_with_keywords_optimized(data, 5)

    # Call the test functions
    test_my()
    test_bot()

if __name__=="__main__":
    data = generate_test_data(5, 5)
    memory_test(data)
    test_graph()