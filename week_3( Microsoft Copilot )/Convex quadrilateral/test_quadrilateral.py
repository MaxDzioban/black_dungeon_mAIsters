'''Test for quadrilateral'''
import unittest
from quadrilateral import *
class TestFunctions(unittest.TestCase):
    def test_lines_intersection(self):
        self.assertEqual(lines_intersection(1, 2, 3, 4), (1, 3))
        self.assertEqual(lines_intersection(1, 1, 1, 2), None)
        self.assertEqual(lines_intersection(0, 0, 0, 0), (0, 0))

    def test_distance(self):
        self.assertEqual(distance(0, 0, 1, 1), 1.41)
        self.assertEqual(distance(0, 0, 3, 4), 5.0)
        self.assertEqual(distance(0, 0, 0, 0), 0.0)

    def test_quadrangle_area(self):
        self.assertEqual(quadrangle_area(3, 4, 3, 4, 5, 5), 12.0)
        self.assertEqual(quadrangle_area(1, 1, 1, 1, 1, 1), 0)
        self.assertEqual(quadrangle_area(0, 0, 0, 0, 0, 0), 0)

    def test_four_lines_area(self):
        # Test with intersecting lines
        self.assertEqual(four_lines_area(1, 0, -1, 0, 0, 1, 0, -1), 4.0)
        # Test with parallel lines
        self.assertEqual(four_lines_area(1, 0, 1, 0, 0, 1, 0, -1), 0)
        # Test with same lines
        self.assertEqual(four_lines_area(0, 0, 0, 0, 0, 0, 0, 0), 0)
        # Test with lines that do not intersect
        self.assertEqual(four_lines_area(1, 0, 1, 1, 1, 2, 1, 3), 0)

if __name__ == '__main__':
    unittest.main()
