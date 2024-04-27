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

# write_csv_file('https://raw.githubusercontent.com/anrom7\
# /Test_Olya/master/New%20folder/total.txt')



import random

if __name__ == "__main__":
    # main()
    # print("hi")
    import time
    import matplotlib.pyplot as plt

    def test_execution_time():
        execution_times_human = []
        execution_times_github = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        input_values = [i for i in range(1, 50)]  # Example input values to test

        for num in input_values:
            start_time = time.time()
            write_csv_file_human('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times_human.append(execution_time)

            start_time = time.time()
            write_csv_file_github('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
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