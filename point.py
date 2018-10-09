from elliptic_curve import EllipticCurve
from sympy import mod_inverse


class Point(object):
    def __init__(self, curve, x, y, mod):
        self.x = x
        self.y = y
        self.curve = curve
        self.mod = mod

        if not curve.is_on_the_curve(x, y, mod):
            raise Exception("The given point {} is not on the curve {}!".format(self, curve))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y, self.mod)

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        x_1, y_1, x_2, y_2 = self.x, self.y, other.x, other.y

        if(x_1, y_2) == (x_2, y_2):
            if y_1 == 0:
                return Ideal(self.curve)
            m = ((3 * x_1 ** 2 + self.curve.a) / (2 * y_1)) % self.mod
        else:
            if x_1 == x_2:
                return Ideal(self.curve)

            m = ((y_2 - y_1) / mod_inverse((x_2 - x_1), self.mod)) % self.mod

        self.x = (m ** 2 - x_2 - x_1) % self.mod
        self.y = (m * (self.x - x_1) + y_1) % self.mod


class Ideal:
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __neg__(self):
        return self

    def __add__(self, other):
        return other


curve = EllipticCurve(-2, 4)

P = Point(curve, 3, 5, 6)
A = Point(curve, -2, 0, 6)
print(P)
P + A
print(P)

