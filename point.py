from elliptic_curve import EllipticCurve


class Point(object):
    def __init__(self, curve, x, y):
        self.x = x
        self.y = y
        self.curve = curve

        if not curve.is_on_the_curve(x, y):
            raise Exception("The given point {} is not on the curve {}!".format(self, curve))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        x_1, y_1, x_2, y_2 = self.x, self.y, other.x, other.y

        if(x_1, y_2) == (x_2, y_2):
            if y_1 == 0:
                return Ideal(self.curve)
            m = (3 * x_1 * x_1 + self.curve.a) / (2 * y_1)
        else:
            if x_1 == x_2:
                return Ideal(self.curve)

            m = (y_2 - y_1) / (x_2 - x_1)

        self.x = m * m - x_2 - x_1
        self.y = m * (self.x - x_1) + y_1


class Ideal:
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __neg__(self):
        return self

    def __add__(self, other):
        return other


C = EllipticCurve(a=-2, b=4)
P = Point(C, 3, 5)
Q = Point(C, -2, 0)
P+Q
print(P)
Q+P
print(Q)
Q+Q
print(Q)
P+P
print(P)
