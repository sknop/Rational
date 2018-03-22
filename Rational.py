from __future__ import print_function


def gcd(x,y):
    if x == 0:
        return abs(y)
    else:
        return gcd(y % x, x)


class Rational:
    def __init__(self, x, y=1):
        _gcd = gcd(x,y)
        self.nomin = x // _gcd
        self.denom = y // _gcd

        if self.denom < 0:
            self.nomin = - self.nomin
            self.denom = - self.denom

    def __str__(self):
        if self.denom > 1:
            return "{} / {}".format(self.nomin, self.denom)
        else:
            return "{}".format(self.nomin)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.nomin * other.denom + other.nomin * self.denom, self.denom * other.denom)
        elif isinstance(other, int):
            return Rational(self.nomin + other * self.denom, self.denom)
        else:
            raise Exception("Cannot add object of type {} to a Rational object".format(other.__class__))

    def __radd__(self, other):
        if isinstance(other, int):
            return Rational(self.nomin + other * self.denom, self.denom)
        else:
            raise Exception("Cannot add object of type {} to a Rational object".format(other.__class__))

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.nomin * other.denom - other.nomin * self.denom, self.denom * other.denom)
        elif isinstance(other, int):
            return Rational(self.nomin - other * self.denom, self.denom)
        else:
            raise Exception("Cannot subtract object of type {} to a Rational object".format(other.__class__))

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other * self.denom - self.nomin, self.denom)
        else:
            raise Exception("Cannot subtract object of type {} to a Rational object".format(other.__class__))

    def __neg__(self):
        return Rational(- self.nomin, self.denom)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.nomin * other.nomin, self.denom * other.denom)
        elif isinstance(other, int):
            return Rational(self.nomin * other, self.denom)
        else:
            raise Exception("Cannot multiply object of type {} to a Rational object".format(other.__class__))

    def __rmul__(self, other):
        if isinstance(other, int):
            return Rational(self.nomin * other, self.denom)
        else:
            raise Exception("Cannot multiply object of type {} to a Rational object".format(other.__class__))

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.nomin * other.denom, self.denom * other.nomin)
        elif isinstance(other, int):
            return Rational(self.nomin, self.denom * other)
        else:
            raise Exception("Cannot divide a Rational object with an object of type {}".format(other.__class__))

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(self.denom * other, self.nomin)
        else:
            raise Exception("Cannot divide a Rational object with an object of type {}".format(other.__class__))
