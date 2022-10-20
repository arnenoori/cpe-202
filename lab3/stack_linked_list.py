class StackLinkedList:
    """Implements an efficient last-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.num_items = 0  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == []

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def push(self, item):
        """Adds item to the stack"""
        # might need to check if full
        if self.is_full():
            raise IndexError
        self.num_items += 1
        addstack = self.Node(item)
        addstack.next_node = self.head
        self.head = addstack
    # doesn't have to return anything

    def pop(self):
        """Returns the current top of the stack"""
        # might have to check if empty
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        addstack = self.head.item
        self = self.head.next_node
        return addstack

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        return self.head.item

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        if self.is_empty():
            return 0
        return self.num_items


def is_balanced(string):
    stack = StackLinkedList(7)
    open_character = {"]":"[", ")": "(", "}":"{"}
    for character in string:
        if character in ["[", "(", "{"]:
            stack.push(character)
        elif character in ["]", ")", "}"]:
            if stack.is_empty():
                return False
            elif stack.pop() != open_character[character]:
                return False
    return stack.is_empty()

'''
str = '(Hello) { world }
for c in str
for i in rang(len(Str)):
    str[i]
math = { '' '' ''}

'''

