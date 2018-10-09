
class EllipticCurve(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if not self.is_smooth():
            raise Exception("{} {} points make not smooth {} curve!".format(a, b, self))

    def is_smooth(self):
        return -16 * (4 * self.a ** 3 + 27 * self.b ** 2) != 0

    def is_on_the_curve(self, x, y, mod):
        return (y ** 2) % mod == (x ** 3 + self.a * x + self.b) % mod

    def __str__(self):
        return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)
