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
        self.root = None

    def insert(self, value):
        """Insert a value in to the binary search tree."""
        if self.root is None:
            self.root = Node(value)
            self._size = 1
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    self._size += 1
                    break
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    self._size += 1
                    break
            else:
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

    def depth(self, start_node=None):
        """Return the depth of the BST."""
        if start_node is None:
            current_node = self.root
        else:
            current_node = start_node
        left_depth = 0
        right_depth = 0
        if current_node.right:
            right_depth += 1
            right_depth += self.depth(current_node.right)
        if current_node.left:
            left_depth += 1
            left_depth += self.depth(current_node.left)
        depth = right_depth if right_depth > left_depth else left_depth
        return depth

    def contains(self, value):
        """Check if the Binary Search Tree has a given value."""
        if self.root:
            current_node = self.root
        else:
            return False
        while True:
            if value == current_node.value:
                return True
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    return False
            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    return False

    def balance(self):
        """Return numerical representation of how balanced the tree is."""
        if self.root.left:
            depth_left = self.depth(self.root.left)
        else:
            depth_left = 0
        if self.root.right:
            depth_right = self.depth(self.root.right)
        else:
            depth_right = 0
        balance = depth_right - depth_left
        return balance
