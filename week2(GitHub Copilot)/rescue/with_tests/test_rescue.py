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
    import time
    import matplotlib.pyplot as plt

    def test_execution_time():
        execution_times_human = []
        execution_times_github = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        input_values = [i for i in range(1, 1000, 25)]  # Example input values to test

        for num in input_values:
            limit = random.randint(1, 250)
            with open('smart_test.txt', 'w', encoding='utf-8') as file:
                file.write('fdfdf\n')
                for i in range(num):
                    file.write("".join(random.choice(alphabet) for _ in range(5)) + "," + str(random.randint(1, 250)) + "\n")
            dic = read_file('smart_test.txt')
            start_time = time.time()
            rescue_people_himan(dic, limit)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times_human.append(execution_time)

            start_time = time.time()
            optimize_rescue(dic, limit)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times_github.append(execution_time)

        plt.plot(input_values, execution_times_human, color = 'red', label = 'human')
        plt.plot(input_values, execution_times_github, color = 'blue', label = 'bot')
        
        plt.xlabel('Input Value')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time vs Input Value')
        plt.legend()
        plt.show()

    test_execution_time()