import unittest
import tempfile
from dictionary import dict_reader_tuple, dict_reader_dict, dict_invert
class TestYourModule(unittest.TestCase):

    def test_dict_reader_tuple_empty_file(self):
        with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
            _ = tmpfile.write('')
        self.assertEqual(dict_reader_tuple(tmpfile.name), ())

    def test_dict_reader_dict_empty_file(self):
        with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
            _ = tmpfile.write('')
        self.assertEqual(dict_reader_dict(tmpfile.name), {})

    def test_dict_invert_empty_dict(self):
        self.assertEqual(dict_invert({}), {})

    def test_dict_reader_tuple_multiple_lines(self):
        with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
            _ = tmpfile.write('NACHOS 2 N AE1 CH OW0 Z\\nTACOS 1 T AA1 K OW0 Z')
        self.assertEqual(dict_reader_tuple(tmpfile.name), (('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z']), ('TACOS', 1, ['T', 'AA1', 'K', 'OW0', 'Z'])))

    def test_dict_reader_dict_multiple_lines(self):
        with tempfile.NamedTemporaryFile(mode = 'w+', delete=False, encoding='utf-8') as tmpfile:
            _ = tmpfile.write('NACHOS 1 N AA1 CH OW0 Z\\nNACHOS 2 N AE1 CH OW0 Z\\nTACOS 1 T AA1 K OW0 Z')
        self.assertEqual(dict_reader_dict(tmpfile.name), {'NACHOS': {('N', 'AA1', 'CH', 'OW0', 'Z'), ('N', 'AE1', 'CH', 'OW0', 'Z')}, 'TACOS': {('T', 'AA1', 'K', 'OW0', 'Z')}})

    def test_dict_invert_multiple_entries(self):
        self.assertEqual(dict_invert({'WATER':{('W','A','T','E','R')}, 'EARTH':{('E','A','R','T','H')}}), {1: {('WATER', ('W', 'A', 'T', 'E', 'R')), ('EARTH', ('E', 'A', 'R', 'T', 'H'))}})

# if __name__ == '__main__':
#     unittest.main()

