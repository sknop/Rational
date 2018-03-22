from __future__ import print_function

from Rational import Rational
import unittest


class TestRational(unittest.TestCase):
    def testCreate(self):
        a = Rational(1,2)

        self.assertEqual(a.nomin, 1)
        self.assertEqual(a.denom, 2)

    def testNomalisation(self):
        a = Rational(2,4)

        self.assertEqual(a.nomin, 1)
        self.assertEqual(a.denom, 2)

    def testAdd(self):
        a = Rational(1,2)
        b = Rational(1,3)

        c = a + b

        self.assertEqual(c.nomin, 5)
        self.assertEqual(c.denom, 6)

        d = a + 1

        self.assertEqual(d.nomin, 3)
        self.assertEqual(d.denom, 2)

        e = 1 + a

        self.assertEqual(e.nomin, 3)
        self.assertEqual(e.denom, 2)

if __name__ == '__main__':
    unittest.main()
