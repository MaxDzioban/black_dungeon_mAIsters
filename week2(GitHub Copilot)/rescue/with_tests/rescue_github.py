"""
This module contains functions for performing a rescue operation on a group of 
people based on their intelligence quotient (IQ).
"""

def read_file(file_path: str) -> dict:
    """
    Read a file and return its contents as a dictionary.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: The contents of the file as a dictionary.

    Example:
        >>> read_file('data.txt')
        {'name1': 10, 'name2': 20, 'name3': 30}
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return_dict = {}
    for i in data:
        i = i.strip()
        i = i.split(',')
        if i[-1].isnumeric():
            return_dict.setdefault(i[0], int(i[1]))
    return return_dict


def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    """
    Perform a rescue operation on a group of people based on their intelligence quotient (IQ).

    Args:
        smarties (dict): A dictionary mapping people's names to their IQ.
        limit_iq (int): The maximum IQ limit for each rescue trip.

    Returns:
        tuple: A tuple containing the number of rescue trips and the list of people in each trip.

    Example:
        >>> rescue_people({'Alice': 10, 'Bob': 20, 'Charlie': 30}, 25)
        (2, [['Charlie'], ['Bob', 'Alice']])
    """
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
    """
    Optimize the rescue operation by combining multiple trips if possible.

    Args:
        smarties (dict): A dictionary mapping people's names to their IQ.
        limit_iq (int): The maximum IQ limit for each rescue trip.

    Returns:
        tuple: A tuple containing the number of rescue trips and the list of people in each trip.

    Example:
        >>> optimize_rescue({'Alice': 10, 'Bob': 20, 'Charlie': 30}, 25)
        (2, [['Charlie'], ['Bob', 'Alice']])
    """
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
