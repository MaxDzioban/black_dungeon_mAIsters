import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import memory_usage
# import parallelTestModule
import random

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def read_input_file_github(url: str, number: int) -> list[list[str]]:
    umovn_list = []
    with urllib.request.urlopen(url) as webpage:
        if number == 0:
            return umovn_list
        for line in webpage:
            line = line.strip().decode('utf-8')
            if line[0].isdigit():
                temp_list = line.split("\t")
                umovn_list.append(temp_list[:2])
                if temp_list[2] == "До наказу" or temp_list[2] == "Рекомендовано (контракт)":
                    umovn_list[-1].insert(2, "+")
                umovn_list[-1].append(temp_list[3])
            if line.startswith("Середній"):
                umovn_list[-1].append(line.split()[-1])
            if line.startswith("—"):
                umovn_list[-1][2] = "+" if umovn_list[-1][2] != "Рекомендовано (контракт)" else "—"
            if len(umovn_list) == number and len(umovn_list[-1]) == 5:
                return umovn_list

def write_csv_file_github(url: str):
    with open('total.csv', "w", encoding="UTF-8") as failik:
        failik.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        ls = read_input_file_github(url, 77)
        for i in ls:
            failik.write(','.join(i) + '\n')

# write_csv_file_github('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')


'''
This program contains two functions, the first turns url-text into list, 
which contains others lists, where are information about students. 
The second one writes list into .csv file.
'''

import urllib.request
import ssl
# Вимкнення перевірки сертифікатів SSL
ssl._create_default_https_context = ssl._create_unverified_context

def read_input_file_human(url: str, number: int) -> list[list[str]]:
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

def write_csv_file_human(url: str):
    '''
    write_csv_file('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
    '''
    with open('total.csv',"w", encoding="UTF-8") as failik:
        failik.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.')
        failik.write("\n")
        ls = read_input_file_human(url, 77)
        #for i in ls:
        #counter = 1
        #for i in ls:
            #for idx, z in enumerate(i):
               # failik.write(z)
              #  if idx < len(i) - 1:
             #       failik.write(",")
            #if counter < len(ls):
            #    failik.write("\n")
            #counter += 1

        counter = 1
        for i in ls:
            for idx, z in enumerate(i):
                failik.write(z)
                if idx < len(i) - 1:
                    failik.write(',')
            if counter < len(ls):
                failik.write('\n')
            counter += 1

def memory_test():
    mem_usages_1 = []
    mem_usages_2 = []
    # Different input values
    input_values = [i for i in range(1, 5)]  # Example input values to test

    for num in input_values:
#             write_csv_file_human('https://raw.githubusercontent.com/anrom7\
# /Test_Olya/master/New%20folder/total.txt')
            m1 = memory_usage((write_csv_file_human, (('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt'),), {}))
            mem_usages_1.append(m1[-1])

            m2 = memory_usage((write_csv_file_github, (('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt'),), {}))
            mem_usages_2.append(m2[-1])
    # Plot the results
    plt.plot(mem_usages_1, label = 'human')
    plt.plot(mem_usages_2, label = 'GitHub Copilot')
    plt.title('Memory Usage vs. Input Value')
    plt.xlabel('Input Value')
    plt.ylabel('Memory Usage (MB)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':    
    memory_test()
