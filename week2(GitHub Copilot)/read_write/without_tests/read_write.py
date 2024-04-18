'''
This program contains two functions, the first turns url-text into list, 
which contains others lists, where are information about students. 
The second one writes list into .csv file.
'''

import urllib.request
import ssl
# Вимкнення перевірки сертифікатів SSL
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
    with urllib.request.urlopen(url) as webpage:
        if number == 0:
            return umovn_list
        for line in webpage:
            line=line.strip().decode('utf-8')
            if line[0].isdigit():
                temp_list=line.split("\t")
                umovn_list.append(temp_list[:2])
                if temp_list[2] in ["До наказу", "Рекомендовано (контракт)"]:
                    umovn_list[-1].insert(2, "+")
                umovn_list[-1].extend(temp_list[3:])
            if line.startswith("Середній"):
                umovn_list[-1].append(line.split()[-1])
            if line.startswith("—"):
                umovn_list[-1][2] = line.split("\t")[-1] if line.split("\t")[-1] != "+" else "—"
            if len(umovn_list)==number and len(umovn_list[-1]) == 5:
                return umovn_list

def write_csv_file(url: str):
    '''
    write_csv_file('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
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

write_csv_file('https://raw.githubusercontent.com/anrom7\
/Test_Olya/master/New%20folder/total.txt')
