
def find_films_with_keywords_github(film_keywords: dict, num_of_films: int):
    '''
    Returns list of the films with the highest number of tags
    >>> find_films_with_keywords({'number-in-title1':['sasat1','assat1']\
,'number-in-title2':['assat1','sasat3','sasat1']},3)
    [('assat1', 2), ('sasat1', 2), ('sasat3', 1)]
    >>> find_films_with_keywords({'number-in-title1':['sasat1','sasat2']\
,'number-in-title2':['sasat1','sasat3']},2)
    [('sasat1', 2), ('sasat2', 1)]
    >>> find_films_with_keywords({'====================': ['===================='], '': [''], \
'number-in-title': ['"#1 Single" (2006)'], 'web-series': \
['"#1MinuteNightmare" (2014)', '"#ATown" (2014)'], 'friend': \
['"#30Nods" (2016)'], 'heroin': ['"#30Nods" (2016)'], 'vlog': \
['"#30Nods" (2016)'], 'austin-texas': ['"#ATown" (2014)'], 'beer': \
['"#ATown" (2014)'], 'drugs': ['"#ATown" (2014)'], 'friendship': \
['"#ATown" (2014)'], 'love': ['"#ATown" (2014)'], 'texas': \
['"#ATown" (2014)'], 'tv-mini-series': ['"#Bandcamp" (2014)']},2)
    [('"#ATown" (2014)', 7), ('"#30Nods" (2016)', 3)]
    '''
    max_dict = {}
    for value in film_keywords.values():
        for i in value:
            max_dict[i] = max_dict.get(i, 0) + 1
    output = sorted(max_dict.items(), key=lambda x: (-x[1], x[0]))[:num_of_films]
    return [(film, count) for film, count in output]

def find_films_with_keywords_human(film_keywords: dict, num_of_films: int):
    '''
    Returns tuple with (film name, max_keywords)
    >>> find_films_with_keywords({'gonki': ['nfs_mw', 'dark souls'], 'tututu': ['dark souls', \
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

def find_films_with_keywords_bohdan(film_keywords: dict, num_of_films: int)->list:
    '''
    Returns list of the films with the highest number of tags
    >>> find_films_with_keywords({'number-in-title1':['sasat1','assat1']\
,'number-in-title2':['assat1','sasat3','sasat1']},3)
    [('assat1', 2), ('sasat1', 2), ('sasat3', 1)]
    >>> find_films_with_keywords({'number-in-title1':['sasat1','sasat2']\
,'number-in-title2':['sasat1','sasat3']},2)
    [('sasat1', 2), ('sasat2', 1)]
    >>> find_films_with_keywords({'====================': ['===================='], '': [''], \
'number-in-title': ['"#1 Single" (2006)'], 'web-series': \
['"#1MinuteNightmare" (2014)', '"#ATown" (2014)'], 'friend': \
['"#30Nods" (2016)'], 'heroin': ['"#30Nods" (2016)'], 'vlog': \
['"#30Nods" (2016)'], 'austin-texas': ['"#ATown" (2014)'], 'beer': \
['"#ATown" (2014)'], 'drugs': ['"#ATown" (2014)'], 'friendship': \
['"#ATown" (2014)'], 'love': ['"#ATown" (2014)'], 'texas': \
['"#ATown" (2014)'], 'tv-mini-series': ['"#Bandcamp" (2014)']},2)
    [('"#ATown" (2014)', 7), ('"#30Nods" (2016)', 3)]
    '''
    process_dict={}
    for _,value in film_keywords.items():
        for i in value:
            process_dict.setdefault(i,0)
            process_dict[i]+=1
    sorted_dict=sorted(process_dict.items(),key=lambda x: x[0])
    sorted_dict=sorted(sorted_dict,key=lambda x: x[1],reverse=True)
    return sorted_dict[:num_of_films]

import random

if __name__ == "__main__":
    # main()
    # print("hi")
    import time
    import matplotlib.pyplot as plt
    from memory_profiler import memory_usage

    def test_execution_time():
        memory_human = []
        memory_github = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        input_values = [i for i in range(1, 2000, 100)]  # Example input values to test

        for num in input_values:
            dic = {}
            num_of_films = num//2
            for i in range(num):
                dic["".join(random.choice(alphabet) for _ in range(10))] = ["".join(random.choice(alphabet) for _ in range(5) for i in range(5))]
            m1 = memory_usage((find_films_with_keywords_human, (dic, num_of_films,), {}))
            memory_human.append(m1[-1])

            m2 = memory_usage((find_films_with_keywords_github, (dic, num_of_films,), {}))
            memory_github.append(m2[-1])


        plt.plot(input_values, memory_human, color = 'red', label = 'human')
        plt.plot(input_values, memory_github, color = 'blue', label = 'bot')
        
        plt.xlabel('Input Value')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time vs Input Value')
        plt.legend()
        plt.show()

    test_execution_time()