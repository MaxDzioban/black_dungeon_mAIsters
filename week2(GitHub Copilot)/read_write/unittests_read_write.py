import unittest
from read_write.with_tests.read_write import read_input_file, write_csv_file

class TestReadInputFile(unittest.TestCase):
    def test_case_1(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        result = read_input_file(url, 1)
        expected = [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
        self.assertEqual(result, expected)

    def test_case_2(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        result = read_input_file(url, 2)
        expected = [['1', 'Мацюк М. І.', '+', '197.859', '10.80'],
                    ['2', 'Проць О. В.', '+', '197.152', '11.60']]
        self.assertEqual(result, expected)

    def test_case_3(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        result = read_input_file(url, 3)
        expected = [['1', 'Мацюк М. І.', '+', '197.859', '10.80'],
                    ['2', 'Проць О. В.', '+', '197.152', '11.60'],
                    ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
        self.assertEqual(result, expected)

    def test_case_4(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        result = read_input_file(url, 4)
        expected = [['1', 'Мацюк М. І.', '+', '197.859', '10.80'],
                    ['2', 'Проць О. В.', '+', '197.152', '11.60'],
                    ['3', 'Лесько В. О.', '+', '195.385', '10.60'],
                    ['4', 'Дмитрук А. Д.', '+', '189.123', '11.50']]
        self.assertEqual(result, expected)

    def test_case_0(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        result = read_input_file(url, 0)
        expected = []
        self.assertEqual(result, expected)

class TestWriteCsvFile(unittest.TestCase):
    def test_write_csv_file(self):
        url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
        write_csv_file(url)
        with open('total.csv', 'r', encoding='UTF-8') as csvfile:
            csv_data_result = csvfile.readlines()
        with open('check.csv', 'r', encoding='UTF-8') as csvfile:
            csv_data = csvfile.readlines()
            self.assertTrue(csv_data_result,csv_data)
if __name__ == '__main__':
    unittest.main()
