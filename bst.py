class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key # unique value
        self.data = None

        # insert()
            # newNode = Node(key)
            # newNode.data = "
        # b.right = d
    def insert(self, key):
        if self.key != None:
            if key < self.key:
                if self.left = None:
                    self.left = TreeNode(key)
                else:
                    self.left.inesrt(key)
            elif key > self.key
                if self.right = None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    def find_successor(self):
        if self.right != None:
            return.self.right.helper_successor()
        current = self
        while current.parent != None and current.parent.right is current:
            current = current.parent
        return current.parent
    def helper_successor(self):
        current = self
        while current.left != None:
            current = current.left
        return current

    def helper_delete(self, key):
        if self.key == key:
            if self.right and self.left:
                [nextsuccessor, successor] = self.right.helper_Find_Min(self)
                if nextsuccesor.left == successor
                    nextsuccesor.left = succesor.right
                else:
                    nextsuccesor.right = succesor.right
                successor.left = self.left
                succesor.right = self.right
                return succesor

            # missing rest of argument
    def helper_Find_Min(self, parent):
        if self.left:
            return self.left.helper_Find_Min(self)
        else:
            return [parent, self]

    def find_max(self):
        if self.right is not None:
            return self.right.find_max()
        else:
            return self.key


    # not sure if I need these but I might:

    def inorder_print_tree(self)

    def helper_print_tree(self):
        # kind of does the same thing as print tree

class BinarySearchTree:
# write the __init__() method here. The tree has at least a ‘root’ node.
    def __init__(self, root):
        self.root = None
        # node
        # size
        # height

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

# test by Min.

    def find_max(self):  # returns max value in the tree
        if node is not None:
            while node.right is not None:
                node = node.right
        return node

# test by Max.

    def insert(self, newkey): # inserts a node with key into the correct position if not a duplicate.
        if self.root is None:
            self.root = TreeNode(newkey)
            return
        else:
            succesor = self.root
            if  succesor.key > newkey:
                if succesor.left is None:
                    succesor.left = TreeNode(newkey)
                else:
                    successor.left.insert(newkey)
            else:
                if succesor.right is None:
                    succesor.right = TreeNode(newkey)
                else:
                    successor.right.insert(newkey)


        # takes a bit longer to do
        # def_insert(node, item)


    def delete(self, key):  # deletes the node containing key, assumes such a node exists
        if self.root:
            self.root = self.root.helper_delete(key)
        # takes a bit longer to do

    def print_tree(self):  # print inorder the entire tree
            if self.root is not None:
                print("Tree is printing:")
                self.root.inorder_print_tree()
        # same thing as inorder_print_tree

    def is_empty(self):  # returns True if tree is empty, else False
        if self.root  is None:
            return True
        else:
            return False

    def inorder_print_tree(self): # print inorder the subtree of self

        # same thing as print_tree only one is necessary

    def print_levels(self):  # inorder traversal prints list of pairs, [key, level of the node] where root is level 0

