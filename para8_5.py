import unittest
from main import *


class MyTest(unittest.TestCase):
    def test_arg(self):
        self.assertEquals(adder(2, 2), 4)

    def test_kwarg(self):
        self.assertEquals(adder(a=10, b=11), 21)

    def test_mixed(self):
        self.assertEquals(adder(1, c=45), 46)

    def test_dif(self):
        x = 10
        y = 0
        self.assertEquals(adder(0, -5, y, a=x),5)

    def test_wrong_type(self):
        self.assertEquals(adder("5", "adc", 10),15)


if __name__ == "__main__":
    unittest.main()

