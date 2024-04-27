import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import memory_usage


import random

def read_file(file_path:str)->dict:
    '''
    Read from file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w',delete=False) as tmp:
    ...     _=tmp.write('AB,200\\nBC,200\\nID,250\\nIB,250\\nOC,300\\nOD,300\\ni,350')
    >>> read_file(tmp.name)
    {'AB': 200, 'BC': 200, 'ID': 250, 'IB': 250, 'OC': 300, 'OD': 300, 'i': 350}
    '''
    with open(file_path,'r',encoding='utf-8') as file:
        data=file.readlines()
    return_dict={}
    for i in data:
        i=i.strip()
        i=i.split(',')
        if i[-1].isnumeric():
            return_dict.setdefault(i[0],int(i[1]))
    return return_dict

def optimize_rescue(smarties: dict, limit_iq: int) -> tuple:
    output_lst = []
    remaining_people = list(smarties.keys())
    remaining_people.sort(key=lambda x: (-smarties[x], x))
    
    while remaining_people:
        current_trip = []
        current_iq = 0
        
        for person in remaining_people:
            if current_iq + smarties[person] <= limit_iq:
                current_trip.append(person)
                current_iq += smarties[person]
        if not current_trip:
            break
        
        output_lst.append(current_trip)
        remaining_people = [person for person in remaining_people if person not in current_trip]
        
        if not remaining_people:
            break
    
    return len(output_lst), output_lst

def rescue_people_himan(smarties: dict, limit_iq: int) -> tuple:
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


if __name__ == "__main__":
    # main()
    # print("hi")
    def test_execution_time():
        memory_human = []
        memory_github = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        input_values = [i for i in range(1, 5000, 50)]  # Example input values to test

        for num in input_values:
            limit = random.randint(1, 250)
            with open('smart_test.txt', 'w', encoding='utf-8') as file:
                file.write('fdfdf\n')
                for i in range(num):
                    file.write("".join(random.choice(alphabet) for _ in range(5)) + "," + str(random.randint(1, 250)) + "\n")
            dic = read_file('smart_test.txt')
            mem = memory_usage((rescue_people_himan, (dic, limit,), {}))
            memory_human.append(mem[-1])

            mem = memory_usage((optimize_rescue, (dic, limit,), {}))
            memory_github.append(mem[-1])

        print(memory_human)

        print(memory_github)

        plt.plot(input_values, memory_human, color = 'red', label = 'human')
        plt.plot(input_values, memory_github, color = 'blue', label = 'bot')
        
        plt.title('Memory Usage vs. Input Value')
        plt.xlabel('Input Value')
        plt.ylabel('Memory Usage (MB)')

        plt.legend()
        plt.show()

    test_execution_time()


# if __name__ == "__main__":

#     def test_memory():
#         memory_human = []
#         memory_github = []
#         input_values = [i for i in range(1, 20000, 9999)]  # Example input values to test

#         for num in input_values:
#             mem = memory_usage((main_human, (num,), {}))
#             memory_human.append(mem[-1])

#             mem = memory_usage((main_github, (num,), {}))
#             memory_github.append(mem[-1])

#         print(memory_human)

#         print(memory_github)

#         plt.plot(input_values, memory_human, color = 'red', label = 'human')
#         plt.plot(input_values, memory_github, color = 'blue', label = 'bot')
        
#         plt.title('Memory Usage vs. Input Value')
#         plt.xlabel('Input Value')
#         plt.ylabel('Memory Usage (MB)')
#         plt.show()

#         plt.legend()

#     test_memory()
