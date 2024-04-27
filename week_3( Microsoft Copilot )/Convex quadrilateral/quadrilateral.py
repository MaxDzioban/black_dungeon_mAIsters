import math

def lines_intersection(k1, c1, k2, c2):
    """function returns 4 numbers(int or float) --> tuple with lines intersection
    if lines are paralel - None"""
    if abs(k1 - k2) < 1e-6:
        return None
    x = (c2 - c1) / (k1 - k2)
    y = k1*x + c1
    return (round(x,2), round(y,2))

def distance(x1,y1,x2,y2):
    """function returns of 2 lines """
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return round(dist, 2) if dist > 0.01 else 0

def quadrangle_area(a, b, c, d, f1, f2):
    """function contstains 6 parsametrs, which are lens of sides and
    lens of diagonals, --> return square of rectangle"""
    if (a+b<=f1) or (b+c<=f2) or (c+d<=f1) or (d+a<=f2) or any(i <= 0 for i in [a, b, c, d, f1, f2]):
        return 0
    s = 0.25*((4*f1**2*f2**2-(b**2+d**2-a**2-c**2)**2)**0.5)
    return round(s,2) if s > 0.01 else 0

def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """функціональна декомпозиція"""
    side1 = lines_intersection(k1, c1, k2, c2)
    side2 = lines_intersection(k2, c2, k3, c3)
    side3 = lines_intersection(k3, c3, k4, c4)
    side4 = lines_intersection(k4, c4, k1, c1)
    if None in (side1, side2, side3, side4):
        return 0
    a = distance(side1[0], side1[1], side2[0], side2[1])
    b = distance(side2[0], side2[1], side3[0], side3[1])
    c = distance(side3[0], side3[1], side4[0], side4[1])
    d = distance(side4[0], side4[1], side1[0], side1[1])
    f1 = distance(side1[0], side1[1], side3[0], side3[1])
    f2 = distance(side2[0], side2[1], side4[0], side4[1])
    return quadrangle_area(a, b, c, d, f1, f2)
