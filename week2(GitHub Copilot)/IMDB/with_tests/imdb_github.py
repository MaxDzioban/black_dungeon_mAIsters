def find_films_with_keywords(film_keywords: dict, num_of_films: int):
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



