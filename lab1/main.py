def indexOf(text, string,index=0):
    if text == None or string == None: return -1
    if len(string) > len(text): return -1
    if len(text) == len(string) and not text.startswith(string): return -1
    if text.startswith(string): return index
    return indexOf(text[1:], string,index+1)
# print(indexOf("peanut", "pea"))
# print(indexOf("Mississippi", "sip"))
# print(indexOf("water", "ter"))
# print(indexOf("California", "sip"))
def squareRootGuess(x, g = 1.0):
    if abs(x - (g*g)) < 0.0000001: return g
    # while (x != g**g):
    # guess = (x, (g + (x / g))/2.0)
    return squareRootGuess(x, (g + (x / g))/2.0)
# print(squareRootGuess((4)))
# print(squareRootGuess((9)))
# print(squareRootGuess((16)))
# print(squareRootGuess((25)))
# print(squareRootGuess((36)))


    # create function file and then test cases file, compute the square root of a number given certain parameters, test edge conditions such as a negative number or zero
    # x = 4
    # g = 1
    # ng = (g+x/g)/2 < problem reduction
    # should return 2.05
    # recursion (loop) to call 6 decimal points
    # sqrt(n, g=1)
    # s = sqrt(4)
    # Base case ng*ng == x (or 4 in this example)
    # if(ng*ng == X)
        # returning
    # else

# |x-ng^2| > epsilon
# def square_root(x, g=1):

import unittest
from main import *
#unittest.main()
# def to_be_tested(): return -1
# class Testings(unittest2.TestCase):
    # def test_it(self): self.assertEqual(to_be_tested(), -1)

class TestCases(unittest.TestCase):
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
        unittest.main()
        print("Tests passed.")


    # https://docs.python.org/3/library/unittest.html





