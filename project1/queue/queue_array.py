class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.head = None
        self.tail = -1
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """Adds item to the queue"""
        if not self.is_full():
            if self.head == None:
                self.head = 0
            self.tail = (self.tail + 1) % self.capacity
            self.items[self.tail] = item
            self.num_items += 1
        else:
            raise IndexError('Index is full')

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise IndexError
        addtoqueue = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        self.num_items -= 1
        return addtoqueue

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.items[self.head]

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        if self.is_empty():
            return 0
        return self.num_items
