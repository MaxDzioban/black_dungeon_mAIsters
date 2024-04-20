"""

https://github.com/MaxDzioban/Dzoban-Maksym-lab8-task1-2.git

There are 4 function in this file
weekday_name() returns a string representing a weekday
weekday() returns an integer representing a weekday 
(0 represents monday and so on)

calendar(month, year) returns a string representing a\
horizontal calendar for the given month and year

fuction transform_calendar()
returns a modified horizontal into vertical calendar
"""
import calendar as cl
import datetime
def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    >>> weekday_name(4)
    'fri'
    >>> weekday_name(16)
    """
    week_day={0:"mon",1:"tue",2:"wed",3:"thu",4:"fri",5:"sat",6:"sun"}
    ailable_number=[0,1,2,3,4,5,6]
    if number not in ailable_number:
        return None
    if not isinstance(number, int):
        return None
    return week_day[number]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError 
    with corresponding message
                                                
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    try:
        day, month, year = map(int, date.split('.'))
        datetime_instance = datetime.datetime(year, month, day)
        day_of_the_week = datetime_instance.weekday()
        return day_of_the_week
    except ValueError:
        return None

def calendar(month_: int, year_: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
    works correctly only for Gregorian calendar, so year must
    be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    formatted_month = cl.month(year_, month_, w=3)
    formatted_month=formatted_month.lower()
    formatted_month_lst=formatted_month.split("\n")
    formatted_month_lst.pop(0)
    fgh="\n".join(formatted_month_lst)
    portu=fgh.rstrip()
    return portu

def transform_calendar(calendar):
    """Transforms a calendar string into a specific format."""
    formatted_month_lst = [
        line for line in calendar.split("\n")[1:] if line.strip() != ''
    ]
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day_lists = {day: [day] for day in days}

    # Create a list of the days in the first week
    first_week = [char for char in formatted_month_lst[0] if char.isdigit()]
    first_week = [" "] * (7 - len(first_week)) + first_week

    for i, day in enumerate(days):
        day_lists[day].append(first_week[i])

    formatted_month_lst = formatted_month_lst[1:]
    last_row = formatted_month_lst[-1].split()
    formatted_month_lst = formatted_month_lst[:-1]
    nested_lists = [list(map(int, s.split())) for s in formatted_month_lst]

    for week in nested_lists:
        for i, day in enumerate(days):
            day_lists[day].append(week[i] if i < len(week) else " ")

    for i, day in enumerate(days):
        day_lists[day].append(last_row[i] if i < len(last_row) else " ")

    weekday_cal = [day_lists[day] for day in days]
    calendar_str = '\n'.join(
        ' '.join(map(str, day)).rstrip() for day in weekday_cal
    )
    return calendar_str


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)
print(transform_calendar(calendar(3, 2022)))
