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

from itertools import combinations

def rescue_people(smarties: dict, limit_iq: int) -> tuple:
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
        
        output_lst.append(current_trip)
        remaining_people = [person for person in remaining_people if person not in current_trip]
    
    return len(output_lst), output_lst
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
        
        output_lst.append(current_trip)
        remaining_people = [person for person in remaining_people if person not in current_trip]
        
        if not remaining_people:
            break
    
    return len(output_lst), output_lst

    # def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    #     return optimize_rescue(smarties, limit_iq)

