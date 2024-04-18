import unittest
from calendar.one_month_calendar import transform_calendar, calendar

class TransformCalendarTestCase(unittest.TestCase):
    def test_transform_calendar(self):
        # Test case 1: January 2022
        expected_output = """mon   3 10 17 24 31
tue   4 11 18 25
wed   5 12 19 26
thu   6 13 20 27
fri   7 14 21 28
sat 1 8 15 22 29
sun 2 9 16 23 30"""
        self.assertEqual(transform_calendar(calendar(1, 2022)), expected_output)

        # Test case 2: February 2022
        expected_output = """mon   7 14 21 28
tue 1 8 15 22
wed 2 9 16 23
thu 3 10 17 24
fri 4 11 18 25
sat 5 12 19 26
sun 6 13 20 27"""
        self.assertEqual(transform_calendar(calendar(2, 2022)), expected_output)

        # Test case 3: March 2022
        expected_output = """mon   7 14 21 28
tue 1 8 15 22 29
wed 2 9 16 23 30
thu 3 10 17 24 31
fri 4 11 18 25
sat 5 12 19 26
sun 6 13 20 27"""
        self.assertEqual(transform_calendar(calendar(3, 2022)), expected_output)

        # Additional test cases...

if __name__ == '__main__':
    unittest.main()