# '''
# This program contains two functions, the first turns url-text into list,
# which contains others lists, where are information about students.
# The second one writes list into .csv file.
# '''
import urllib.request
import csv
import time
import matplotlib.pyplot as plt
import os
import psutil
from memory_profiler import memory_usage, profile
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def read_input_file(url: str, number: int) -> list[list[str]]:
    """
    Preconditions: 0 <= number <= 77
    Return list of strings lists from url
    >>> read_input_file('https://raw.githubusercontent.com/\
anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/\
anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], \
['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    >>> read_input_file('https://raw.githubusercontent.com/\
anrom7/Test_Olya/master/New%20folder/total.txt',4)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], \
['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60'], \
['4', 'Дмитрук А. Д.', '+', '189.123', '11.50']]
    >>> read_input_file('https://raw.githubusercontent.com/\
anrom7/Test_Olya/master/New%20folder/total.txt',0)
    []
    """
    umovn_list=[]
    zeta_yota=[]
    with urllib.request.urlopen(url) as webpage:
        if number == 0:
            return umovn_list
        for line in webpage:
            line=line.strip().decode('utf-8')
            if line[0].isdigit():
                temp_list=line.split("\t")
                umovn_list.append(temp_list[:2])
                if temp_list[2] == "До наказу" or temp_list[2] == "Рекомендовано (контракт)":
                    umovn_list[-1].insert(2, "+")
                umovn_list[-1].append(temp_list[3])
            if line.startswith("Середній"):
                umovn_list[-1].append(line.split()[-1])
            if line.startswith("—"):
                zeta_yota=line.split("\t")
                if zeta_yota[-1] == "+":
                    zeta_yota = []
                    temp_list=[]
                elif temp_list[2] == "Рекомендовано (контракт)":
                    umovn_list[-1][2]="+"
                    zeta_yota = []
                    temp_list=[]
                else:
                    umovn_list[-1][2]="—"
                    zeta_yota = []
                    temp_list=[]
            if len(umovn_list)==number and len(umovn_list[-1]) == 5:
                return umovn_list

def write_csv_file(url: str):
    '''
    write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')
    '''
    with open('total.csv',"w", encoding="UTF-8") as failik:
        failik.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.')
        failik.write("\n")
        ls = read_input_file(url, 77)
        counter = 1
        for i in ls:
            for idx, z in enumerate(i):
                failik.write(z)
                if idx < len(i) - 1:
                    failik.write(',')
            if counter < len(ls):
                failik.write('\n')
            counter += 1

def read_input_file_optimised(url: str, number: int) -> list[list[str]]:
    """
    Reads a webpage and processes its content.

    Args:
        url (str): Webpage URL.
        number (int): Number of lines to process.

    Returns:
        list: Processed lines.

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], \
['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """

    if number == 0:
        return []

    umovn_list = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip().decode('utf-8')
            if line and line[0].isdigit():
                temp_list = line.split("\t")
                umovn_list.append(temp_list[:2])
                if temp_list[2] in ["До наказу", "Рекомендовано (контракт)"]:
                    umovn_list[-1].append("+")
                else:
                    umovn_list[-1].append("—")
                umovn_list[-1].append(temp_list[3])
            if line.startswith("Середній"):
                umovn_list[-1].append(line.split()[-1])
            if umovn_list and len(umovn_list) == number and len(umovn_list[-1]) == 5:
                return umovn_list
    return umovn_list

def write_csv_file_optimised(url: str):
    """
    Writes webpage content to a CSV file.

    Args:
        url (str): Webpage URL.

    >>> write_csv_file('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
    """
    with open('total.csv', "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(['№', 'ПІБ', 'Д', 'Заг.бал', 'С.б.док.осв.'])
        ls = read_input_file_optimised(url, 77)
        writer.writerows(ls)

def memory_test(data):
    @profile
    def test_read_my():
        read_input_file(data, 3)

    @profile
    def test_read_bot():
        read_input_file_optimised(data, 3)

    # Call the test functions
    test_read_my()
    test_read_bot()

if __name__=="__main__":
    data = "https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt"
    memory_test(data)
