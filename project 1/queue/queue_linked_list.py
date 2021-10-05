class QueueLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next_node = None

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.tail = None
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == []

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        """Adds item to the queue"""
        if not self.is_full():
            new_node = self.Node(item)
            if self.tail is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = self.tail.next_node
            self.num_items += 1
        else:
            raise IndexError('Full')

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.num_items == 0:
            raise IndexError
        else:
            data = self.head.item
            if self.head.next_node is None:
                self.head = None
                self.tail = None
            else:
                self.num_items -= 1
                self.head = self.head.next_node
            return data

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.head.item

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        if self.is_empty():
            return 0
        return self.num_items

