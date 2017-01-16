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
        self._size = 0
        self.depth = 0
        self.root = None
        self.depth = 0

    def insert(self, value):
        """Insert a value in to the binary search tree."""
        self._size += 1
        if self.root is None:
            self.root = Node(value)
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break
            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break

    def search(self, value):
        """Search the Binary Search Tree for a value, return node or none."""
        current_node = self.root
        while True:
            if value == current_node.value:
                return current_node
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    return None
            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    return None

    def size(self):
        """Return the size of the BST."""
        return self._size


    def depth(self):
        """Return the depth of the BST."""
        