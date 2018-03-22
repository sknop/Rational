from __future__ import print_function

from Rational import Rational
import unittest


class TestRational(unittest.TestCase):
    def testCreate(self):
        a = Rational(1,2)

        self.assertEqual(a.nomin, 1)
        self.assertEqual(a.denom, 2)

        try:
            b = Rational(1,0)
            self.fail("Did not detect divison by 0")
        except TypeError:
            pass

    def testNormalisation(self):
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

    def testSub(self):
        a = Rational(1,2)
        b = Rational(1,3)

        c = a - b

        self.assertEqual(c.nomin, 1)
        self.assertEqual(c.denom, 6)

        d = a - 1

        self.assertEqual(d.nomin, -1)
        self.assertEqual(d.denom, 2)

        e = 1 - a

        self.assertEqual(e.nomin, 1)
        self.assertEqual(e.denom, 2)

    def testMul(self):
        a = Rational(1,2)
        b = Rational(2,3)

        c = a * b

        self.assertEqual(c.nomin, 1)
        self.assertEqual(c.denom, 3)

        d = b * 2

        self.assertEqual(d.nomin, 4)
        self.assertEqual(d.denom, 3)

        e = 2 * b

        self.assertEqual(e.nomin, 4)
        self.assertEqual(e.denom, 3)

    def testDiv(self):
        a = Rational(1,2)
        b = Rational(1,3)

        c = a / b

        self.assertEqual(c.nomin, 3)
        self.assertEqual(c.denom, 2)

        d = a / 2

        self.assertEqual(d.nomin, 1)
        self.assertEqual(d.denom, 4)

        e = 1 / a

        self.assertEqual(e.nomin, 2)
        self.assertEqual(e.denom, 1)

    def testEqual(self):
        a = Rational(4,5)
        b = Rational(8,10)

        self.assertEqual(a,b)

        c = Rational(2,2)

        self.assertEqual(c, 1)

    def testLessThan(self):
        a = Rational(2,3)
        b = Rational(3,4)

        self.assertTrue(a < b)
        self.assertFalse(b < a)

        self.assertTrue(a < 1)
        # self.assertFalse(1 < a)

if __name__ == '__main__':
    unittest.main()
