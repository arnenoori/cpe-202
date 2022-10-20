import unittest
from bst import *


class Test(unittest.TestCase):

    def test_search(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(21)
        self.assertEqual(tree.insert(5), None)
        self.assertEqual(tree.insert(30), None)
        # self assert False is empty
        # self assert tree height

    def test_height(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(21)
        tree.height()
        self.assertEqual(tree.height(), 4)

    def test_delete(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(4)
        tree.insert(6)
        tree.insert(10)
        tree.insert(9)
        tree.insert(11)
        tree.delete_value(5)
        self.assertTrue(tree.search(5), False)

    def test_insert(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(21)
        self.assertFalse(tree.delete_value(5), "Value already in tree!")

    def test_size(self):
        tree = Bst()
        tree.insert(3)
        tree.insert(2)
        tree.insert(5)
        tree.insert(6)
        self.assertEqual(tree.size, 4)

    def test_is_empty(self):
        tree = Bst()
        tree.insert(1)
        self.assertTrue(tree.is_empty(), False)

    def test_min(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(21)
        tree.insert(5)
        self.assertEqual(tree.min(), [1])

    def test_max(self):
        tree = Bst()
        tree.insert(5)
        tree.insert(2)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(21)
        tree.insert(5)
        self.assertEqual(tree.max(), [21])

if __name__ == '__main__':
    unittest.main()
