'''Rescue people'''
def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    '''
    This function returns a tuple of the number of trips required and a list of lists,
    where each inner list represents a trip and contains the names of the people being
    transported on that trip in the order in which they were chosen by the aliens.

    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": \
195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Person A": 100, "Person B": 200, "Person C": 300, "Person D": 400}, 500)
    (2, [['Person D', 'Person A'], ['Person C', 'Person B']])
    >>> rescue_people({"Person A": 100, "Person B": 200, "Person C": 300, "Person D": 400}, 1000)
    (1, [['Person D', 'Person C', 'Person B', 'Person A']])
    >>> rescue_people({}, 500)
    (0, [])
    >>> rescue_people({"Person A": 100}, 50)
    (0, [])
    '''
    output_lst = []
    limit = limit_iq
    smarties = dict(sorted(smarties.items()))
    smarties = dict(sorted(smarties.items(), key=lambda item: item[1], reverse= True))
    while smarties and limit_iq>max(smarties.values()):
        limit = limit_iq
        trans_lst = []
        for key, value in smarties.items():
            if (limit - value) >= 0:
                trans_lst.append(key)
                limit -= value
        smarties = {k:v for k,v in smarties.items() if k not in trans_lst}
        output_lst.append(trans_lst)
    return (len(output_lst), output_lst)

if __name__=="__main__":
    import doctest
    print(doctest.testmod())
