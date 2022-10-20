import unittest
from stack_linked_list import *

class TestCases(unittest.TestCase):

    def test_is_balanced_1(self):
        self.assertFalse(is_balanced("TEST"))

    def test_is_balanced_2(self):
        self.assertFalse(is_balanced("([test])"))

    def test_is_balanced_3(self):
        self.assertFalse(is_balanced("(test])"))

    def test_is_balanced_4(self):
        self.assertFalse(is_balanced("[{(test)]}"))

    def test_is_balanced_5(self):
        self.assertFalse(is_balanced("[{(test]}"))

    def test_is_balanced_6(self):
        self.assertFalse(is_balanced("[test]]})"))

if __name__ == '__main__':
    unittest.main()
