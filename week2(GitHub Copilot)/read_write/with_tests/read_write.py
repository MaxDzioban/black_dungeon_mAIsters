import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def read_input_file(url: str, number: int) -> list[list[str]]:
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

def write_csv_file(url: str):
    with open('total.csv', "w", encoding="UTF-8") as failik:
        failik.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        ls = read_input_file(url, 77)
        for i in ls:
            failik.write(','.join(i) + '\n')

write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')