"""Classes for binary search tree."""


class Node():
    """Node object for the binary search tree."""

    def __init__(self, value, left=None, right=None):
        """Instantiate a node object."""
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():
    """Binary Search Tree.

    .insert(): Add a value to the BST
    """

    def __init__(self):
        """Initialize the BinarySearchTree Class."""
        self.size = 0
        self.depth = 0
        self.root = None

    def insert(self, value):
        """Insert a value in to the binary search tree."""
        if self.root is None:
            self.root = Node(value)
        current_node = self.root
        while True:
            if value < current_node:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
            if value > current_node:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
