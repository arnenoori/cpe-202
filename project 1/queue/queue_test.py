import unittest
from queue_linked_list import *
from queue_array import *

class MyTestCase(unittest.TestCase):

    # Test cases for Queue Linked List

    def test_is_empty1(self):
        queue = QueueLinkedList(5)
        queue.enqueue(8)
        self.assertFalse(queue.is_empty())

    def test_is_empty2(self):
        queue = QueueLinkedList(6)
        self.assertFalse(queue.is_empty())

    def test_is_full1(self):
        queue = QueueLinkedList(8)
        self.assertFalse(queue.is_full())

    def test_is_full2(self):
        queue = QueueLinkedList(1)
        queue.enqueue(9)
        self.assertTrue(queue.is_full())

    def test_enqueue(self):
        queue = QueueLinkedList(5)
        queue.enqueue(4)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 4)

    def test_dequeue(self):
        queue = QueueLinkedList(9)
        queue.enqueue(8)
        self.assertEqual(queue.dequeue(), 8)

    def test_peek(self):
        queue = QueueLinkedList(6)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 3)

    # Test cases for Queue Array

    def test_is_empty3(self):
        queue = QueueArray(4)
        queue.enqueue(7)
        self.assertFalse(queue.is_empty())

    def test_is_empty4(self):
        queue = QueueArray(4)
        self.assertTrue(queue.is_empty())

    def test_is_full3(self):
        queue = QueueArray(8)
        self.assertFalse(queue.is_full())

    def test_is_full4(self):
        queue = QueueArray(1)
        queue.enqueue(9)
        self.assertTrue(queue.is_full())

    def test_enqueue1(self):
        queue = QueueArray(5)
        queue.enqueue(4)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 4)
       # self.assertEqual(queue.push(), 4)

    def test_dequeue1(self):
        queue = QueueArray(9)
        queue.enqueue(8)
        self.assertEqual(queue.dequeue(), 8)

    def test_peek1(self):
        queue = QueueArray(6)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 3)

if __name__ == '__main__':
    unittest.main()
