import unittest
from binaryheap import *


class Test(unittest.TestCase):
    def test_insert(self):
        binheap = BinaryHeap(5)
        binheap.insert(10)
        binheap.insert(20)
        binheap.insert(5)
        binheap.insert(8)
        binheap.insert(2)
        self.assertEqual(str(binheap), "10 20 5 8 2")

    def test_insert2(self):
        binheap = BinaryHeap(10)
        binheap.insert(5)
        binheap.insert(6)
        binheap.insert(4)
        binheap.insert(2)
        self.assertEqual(str(binheap), "2 4 5 6")

    def test_empty2(self):
        binheap = BinaryHeap(5)
        self.assertTrue(binheap.delMin())

''' 
    def test_empty(self):
        binheap = BinaryHeap(6)
        binheap.insert(5)
        self.assertFalse(binheap.delMin()) # create is_empty?
        
    def test_delete(self):
        binheap = BinaryHeap(2)
        self.assertRaises(binheap.MyException, binheap.delMin)
   
   '''

if __name__ == "__main__":
    unittest.main()

