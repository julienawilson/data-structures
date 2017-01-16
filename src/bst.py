"""Classes for binary search tree."""

class Node():
    def __init__(self, value, left=None, right=None):
        """Instantiate a node object."""
        self.value = value
        self.left = left
        self.right = right
