import unittest
from stack_linked_list import *
from stack_array import *


class MyTestCase(unittest.TestCase):

    # Stack Linked List Testing

    def test_is_empty1(self):
        stack = StackLinkedList(4)
        stack.push(7)
        self.assertFalse(stack.is_empty())

    def test_is_empty2(self):
        stack = StackLinkedList(4)
        self.assertFalse(stack.is_empty())

    def test_is_full1(self):
        stack = StackLinkedList(8)
        self.assertFalse(stack.is_full())

    def test_is_ful2l(self):
        stack = StackLinkedList(1)
        stack.push(9)
        self.assertTrue(stack.is_full())

    def test_push(self):
        stack = StackLinkedList(5)
        stack.push(4)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 4)

    def test_pop(self):
        stack = StackLinkedList(9)
        stack.push(8)
        self.assertEqual(stack.pop(), 8)

    def test_peek(self):
        stack = StackLinkedList(6)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

        # Stack Array Testing

    def test_is_empty3(self):
        stack = StackArray(4)
        stack.push(7)
        self.assertFalse(stack.is_empty())

    def test_is_empty4(self):
        stack = StackArray(4)
        self.assertTrue(stack.is_empty())

    def test_is_full3(self):
        stack = StackArray(8)
        self.assertFalse(stack.is_full())

    def test_is_full4(self):
        stack = StackArray(1)
        stack.push(9)
        self.assertTrue(stack.is_full())

    def test_push1(self):
        stack = StackArray(5)
        stack.push(4)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 4)

    def test_pop1(self):
        stack = StackArray(9)
        stack.push(8)
        self.assertEqual(stack.pop(), 8)

    def test_peek1(self):
        stack = StackArray(6)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)


if __name__ == '__main__':
    unittest.main()
