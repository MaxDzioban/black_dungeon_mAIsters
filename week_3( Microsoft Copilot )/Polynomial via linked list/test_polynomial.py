import unittest
from polynomial import *
class TestMono(unittest.TestCase):
    def test_init(self):
        m = Mono(2, 3)
        self.assertEqual(m.coefficient, 2)
        self.assertEqual(m.degree, 3)

        m = Mono(0, 3)
        self.assertEqual(m.coefficient, 0)
        self.assertEqual(m.degree, 0)

    def test_str(self):
        m = Mono(2, 3)
        self.assertEqual(str(m), 'Mono: 2x**3')

        m = Mono(-1, 3)
        self.assertEqual(str(m), 'Mono: -x**3')

        m = Mono(0, 3)
        self.assertEqual(str(m), 'Mono: 0')

        m = Mono(1, 0)
        self.assertEqual(str(m), 'Mono: 1')

    def test_repr(self):
        m = Mono(2, 3)
        self.assertEqual(repr(m), 'Mono(coeff=2, degree=3)')

    def test_eq(self):
        m1 = Mono(2, 3)
        m2 = Mono(2, 3)
        self.assertEqual(m1, m2)

        m2 = Mono(2, 2)
        self.assertNotEqual(m1, m2)

        self.assertNotEqual(m1, "Not a Mono object")

    def test_zero_degree(self):
        m = Mono(2, 0)
        self.assertEqual(str(m), 'Mono: 2')

    def test_negative_coefficient(self):
        m = Mono(-2, 3)
        self.assertEqual(str(m), 'Mono: -2x**3')

class TestPolynomial(unittest.TestCase):
    def test_init(self):
        m = Mono(2, 3)
        p = Polynomial(m)
        self.assertEqual(p.head, m)

        p2 = Polynomial(p)
        self.assertEqual(p2.head, m)

        with self.assertRaises(TypeError):
            p3 = Polynomial("Not a Mono or Polynomial object")

    def test_str(self):
        m1 = Mono(2, 3)
        m2 = Mono(-1, 2)
        p = Polynomial(m1, m2)
        self.assertEqual(str(p), 'Polynomial: 2x**3-x**2')

        m1 = Mono(0, 0)
        m2 = Mono(0, 0)
        p = Polynomial(m1, m2)
        self.assertEqual(str(p), 'Polynomial: 0')

    def test_degree(self):
        m = Mono(2, 3)
        p = Polynomial(m)
        self.assertEqual(p.degree, 3)

        m = Mono(0, 0)
        p = Polynomial(m)
        self.assertEqual(p.degree, 0)

    def test_copy(self):
        m = Mono(2, 3)
        p1 = Polynomial(m)
        p2 = p1.copy()
        self.assertEqual(p1, p2)

    def test_derivative(self):
        m = Mono(2, 3)
        p = Polynomial(m)
        self.assertEqual(p.derivative.head.coefficient, 6)
        self.assertEqual(p.derivative.head.degree, 2)

        m = Mono(0, 0)
        p = Polynomial(m)
        self.assertEqual(p.derivative.head.coefficient, 0)
        self.assertEqual(p.derivative.head.degree, 0)

    def test_eval_at(self):
        m = Mono(2, 3)
        p = Polynomial(m)
        self.assertEqual(p.eval_at(2), 16)

        m = Mono(0, 0)
        p = Polynomial(m)
        self.assertEqual(p.eval_at(2), 0)

    def test_repr(self):
        m = Mono(2, 3)
        p = Polynomial(m)
        self.assertEqual(repr(p), 'Polynomial(Mono(coeff=2, degree=3))')

    def test_sort(self):
        m1 = Mono(2, 3)
        m2 = Mono(1, 4)
        p = Polynomial(m1, m2)
        p.sort()
        self.assertEqual(p.head, m2)
        self.assertEqual(p.head.next, m1)

    def test_simplify(self):
        m1 = Mono(2, 3)
        m2 = Mono(1, 3)
        p = Polynomial(m1, m2)
        p.simplify()
        self.assertEqual(p.head.coefficient, 3)
        self.assertEqual(p.head.degree, 3)

        m1 = Mono(0, 0)
        m2 = Mono(0, 0)
        p = Polynomial(m1, m2)
        p.simplify()
        self.assertEqual(p.head.coefficient, 0)
        self.assertEqual(p.head.degree, 0)

    def test_eq(self):
        m1 = Mono(2, 3)
        m2 = Mono(1, 4)
        p1 = Polynomial(m1, m2)
        p2 = Polynomial(m1, m2)
        self.assertEqual(p1, p2)

        m3 = Mono(1, 2)
        p3 = Polynomial(m1, m3)
        self.assertNotEqual(p1, p3)

        self.assertNotEqual(p1, "Not a Polynomial object")

    def test_zero_degree(self):
        m = Mono(2, 0)
        p = Polynomial(m)
        self.assertEqual(str(p), 'Polynomial: 2')

    def test_negative_coefficient(self):
        m = Mono(-2, 3)
        p = Polynomial(m)
        self.assertEqual(str(p), 'Polynomial: -2x**3')

    def test_multiple_terms(self):
        m1 = Mono(2, 3)
        m2 = Mono(3, 2)
        p = Polynomial(m1, m2)
        self.assertEqual(str(p), 'Polynomial: 2x**3+3x**2')

    def test_derivative_of_constant(self):
        m = Mono(2, 0)
        p = Polynomial(m)
        self.assertEqual(p.derivative.head.coefficient, 0)
        self.assertEqual(p.derivative.head.degree, 0)

    def test_derivative_of_linear_term(self):
        m = Mono(2, 1)
        p = Polynomial(m)
        self.assertEqual(p.derivative.head.coefficient, 2)
        self.assertEqual(p.derivative.head.degree, 0)

    def test_derivative_of_quadratic_term(self):
        m = Mono(2, 2)
        p = Polynomial(m)
        self.assertEqual(p.derivative.head.coefficient, 4)
        self.assertEqual(p.derivative.head.degree, 1)
# if __name__ == '__main__':
#     unittest.main()
