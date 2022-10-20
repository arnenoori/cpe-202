class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class Bst:
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)  # creating new instance of node class
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):  # recursive
        if value < current_node.value:  # inserting a left child
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:  # right child
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Value already in tree!")
        self.size += 1

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left != None:
            return self._find(value, current_node.left.child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)

    def delete_value(self, value):  # deletes integer
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        def min_value_node(n):  # n = node
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:  # case #1 - no children
            if node_parent.left_child == node:
                node_parent.left_child == None
            else:
                node_parent.right_child == None

        if node_children == 1:  # case #2 = 1 child
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent = node_parent

        if node_children == 3:  # case #3 = 2 children
            successor = min_value_node(node.right_child)
            node.value = successor.value
            self.delete_node(successor)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)

    def min(self):
        node = []
        self._min(self.root, node)
        return node

    def _min(self, root, node):
        if root:
            if root.left_child == None:
                node.append(root.value)
            self._min(root.left_child, node)

    def max(self):
        node = []
        self._max(self.root, node)
        return node

    def _max(self, root, node):
        if root:
            if (root.right_child == None):
                node.append(root.value)
            self._max(root.right_child, node)

    def size(self):
        return self.size

    def is_empty(self):  # returns True if tree is empty, else False
        if self.size == 0:
            return True
        else:
            return False


def fill_tree(tree, number_elements=100, max_integer=1000):
    from random import randint
    for _ in range(number_elements):
        current_element = randint(0, max_integer)
        tree.insert(current_element)
    return tree


tree = Bst()
# tree = fill_tree(tree)

tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(7)
tree.insert(9)
tree.insert(21)
tree.insert(5)

print("What's the min? " + str(tree.min()))
print("What's the max? " + str(tree.max()))
print("Is it empty?" + str(tree.is_empty()))
print("tree size: " + str(tree.height()))
tree.print_tree()

print(tree.search(7))
print(tree.search(30))

tree.height()

tree.delete_value(9)

tree.print_tree()

# print("tree height: " + str(tree.height))

'''
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key # unique value
        self.data = None

class BinarySearchTree:
# write the __init__() method here. The tree has at least a ‘root’ node.
    def __init__(self, root):
        self.root = None
        # node
        # size
        # height

    def insert(self, key):
        if self.key is None:
            return TreeNode(key)
        else:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        return self
# do recursively and have a helper function



    def find(self, key):  # returns True if key is in a node of the tree, else False
        current = self.root
        while current is not None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if current is None:
            return False
        else:
            return True

    def find_min(self):  # returns min value in the tree
        if node == None:
            return None
        if node.left == None:
            return node
        return findMin(node.left)

    def find_max(self):  # returns max value in the tree
        if node is not None:
            while node.right is not None:
                node = node.right
        return node


    def delete(self, key):  # deletes the node containing key, assumes such a node exists
        if self.root:
            self.root = self.root.helper_delete(key)
        # takes a bit longer to do

    def print_tree(self):  # print inorder the entire tree
            if self.root is not None:
                print("Tree is printing:")
                self.root.inorder_print_tree()
        # same thing as inorder_print_tree


    def size(self):
        return self.size

    def is_empty(self):  # returns True if tree is empty, else False
        if size == 0:
            return True
        else:
            return False


    def print_levels(self):  # inorder traversal prints list of pairs, [key, level of the node] where root is level 0

'''