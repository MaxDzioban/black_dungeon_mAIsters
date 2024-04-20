'''bello'''

import math
class Polynomial:
    """class Polynomial"""
    def __init__(self, input_list) -> None:
        input_list_copy=list(input_list)
        if not input_list_copy or input_list_copy == [0]:
            self.degree = len(input_list_copy) - 1
            self.coeffs = input_list_copy[::-1]
        else:
            while input_list_copy and input_list_copy[0] == 0:
                input_list_copy.pop(0)
            self.degree = len(input_list_copy) - 1
            self.coeffs = input_list_copy[::-1]
    def __str__(self):
        if self.coeffs == [0]:
            return "Polynomial: 0"
        terms = []
        for i, coeff in enumerate(self.coeffs[::-1]):
            power = self.degree - i
            if coeff != 0:
                if power == 0:
                    terms.append(str(coeff))
                elif power == 1:
                    if coeff == 1:
                        terms.append("x")
                    else:
                        terms.append(f"{coeff}x")
                else:
                    if coeff == 1:
                        terms.append(f"x**{power}")
                    else:
                        terms.append(f"{coeff}x**{power}")
        return "Polynomial: " + "+".join(terms).replace('+-', '-').replace('-1x', '-x')
    def __repr__(self):
        if self.coeffs==[0]:
            return "Polynomial(coeffs=[0])"
        return f'Polynomial(coeffs={self.coeffs[::-1]})'
    def eval_at(self, x):
        "eval"
        result = 0
        for coeff in reversed(self.coeffs):
            result = result * x + coeff
        return result
    def __eq__(self, other):
        '''не працює добре'''
        if isinstance(other, int) and len(self.coeffs) == 1 and self.coeffs[0] == other:
            return True
        if not isinstance(other, Polynomial):
            return False
        return str(self)==str(other)
    def __hash__(self):
        return hash(tuple(self.coeffs))
    def multiply_by_value(self, value):
        '''multiply_by_value'''
        new_coeffs = [coeff * value for coeff in self.coeffs[::-1]]
        return Polynomial(new_coeffs)
    @property
    def derivative(self):
        """derivative"""
        if len(self.coeffs) == 1:
            return Polynomial([0])
        derivativ_e = []
        for i in range(len(self.coeffs)-1):
            derivativ_e.append(self.coeffs[::-1][i] * (len(self.coeffs)-1-i))
        return Polynomial(derivativ_e)
    def __add__(self, other):
        '''works same len'''
        sum_list = [a + b for a, b in zip(self.coeffs, other.coeffs)]
        return Polynomial(sum_list[::-1])
    def __mul__(self, other):
        degree1 = len(self.coeffs) - 1
        degree2 = len(other.coeffs) - 1
        degree_result = degree1 + degree2
        result = [0] * (degree_result + 1)
        for i in range(degree1 + 1):
            for j in range(degree2 + 1):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result[::-1])
class Quadratic(Polynomial):
    '''bello'''
    def __init__(self, coeffs):
        super().__init__(coeffs)
        if len(self.coeffs) != 3:
            raise ValueError('Quadratic polynomial must have exactly 3 coefficients')
        self.a, self.b, self.c = coeffs
    def __repr__(self):
        return f"Quadratic(a={self.a}, b={self.b}, c={self.c})"
    def __str__(self):
        if self.a==1:
            return f"Quadratic: x**2+{self.b}x+{self.c}".replace("+-","-")
        if self.a==-1:
            return f"Quadratic: -x**2+{self.b}x+{self.c}".replace("+-","-")
        apso= f"Quadratic: {self.a}x**2+{self.b}x+{self.c}".replace("+-","-")
        return apso
    @property
    def discriminant(self):
        """discriminant"""
        return self.b**2 - 4*self.a*self.c
    @property
    def number_of_real_roots(self):
        """get_real_roots"""
        discriminant = self.discriminant
        if discriminant < 0:
            return 0
        if discriminant == 0:
            return 1
        return 2
    def get_real_roots(self):
        """get_real_roots"""
        discriminant = self.discriminant
        if discriminant < 0:
            return []
        if discriminant == 0:
            return [-self.b / (2*self.a)]
        root1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
        root2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
        return [min(root1, root2), max(root1, root2)]
