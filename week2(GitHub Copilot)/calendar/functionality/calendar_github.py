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

def transform_calendar(calendar: str) -> str:
    formatted_month_lst = calendar.split("\n")
    formatted_month_lst = formatted_month_lst[1:]
    formatted_month_lst = [line for line in formatted_month_lst if line.strip() != '']

    weekday_cal = [["mon"], ["tue"], ["wed"], ["thu"], ["fri"], ["sat"], ["sun"]]

    for line in formatted_month_lst:
        days = line.split()
        for i, day in enumerate(days):
            weekday_cal[i].append(day)

    calendar_str = '\n'.join(' '.join(map(str, day)) for day in weekday_cal)
    return calendar_str
