class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.items = [None] * capacity  # initializing the stack
        self.head = [None] * capacity  # initializing the stack
        self.num_items = 0  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if self.num_items == self.capacity:
            return True
        return False

    def push(self, item):
        """Adds item to the stack"""
        self.num_items += 1
        self.head[self.num_items - 1] = item
        return self

    def pop(self):
        """Returns the current top of the stack"""
        addtostack = self.head[self.num_items - 1]
        self.head[self.num_items - 1] = None
        self.num_items -= 1
        return addtostack

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        return self.head[self.num_items - 1]

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        if self.is_empty():
            return 0
        return self.num_items
