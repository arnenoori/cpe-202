import unittest2
from main import *
#unittest.main()
# def to_be_tested(): return -1
# class Testings(unittest2.TestCase):
    # def test_it(self): self.assertEqual(to_be_tested(), -1)

class TestCases(unittest2.TestCase):
    def test_indexOf1(self):
        self.assertEqual(indexOf("peanut", "pea"), 0)
    def test_indexOf2(self):
        self.assertEqual(indexOf("Mississippi", "sip"), 6)
    def test_indexOf3(self):
        self.assertEqual(indexOf("water", "ter"), 2)
    def test_indexOf4(self):
        self.assertEqual(indexOf("California", "sip"), -1)

    def test_squareRootGuess1(self):
        self.assertAlmostEqual(squareRootGuess(4), 2)
    def test_squareRootGuess2(self):
        self.assertAlmostEqual(squareRootGuess(9), 3)
    def test_squareRootGuess3(self):
        self.assertAlmostEqual(squareRootGuess(16), 4)
    def test_squareRootGues4(self):
        self.assertAlmostEqual(squareRootGuess(25), 5)
    def test_squareRootGuess5(self):
        self.assertAlmostEqual(squareRootGuess(36), 6)
    if __name__ == '__main__':
        unittest2.main()
        print("Tests passed.")
