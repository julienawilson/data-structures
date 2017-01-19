"""Classes for binary search tree.

Methods include:
insert(self, val): Insert value into tree; if value already exists, ignore it.
search(self, val): Return node containing that value, else None.
size(self): Return number of nodes/vertices in tree, 0 if empty.
depth(self): Return number of levels in tree. Tree with one value has depth of 0.
contains(self, val): Return True if value is in tree, False if not.
balance(self): Return a positive or negative integer representing tree's balance.
    Trees that are higher on the left than the right should return a positive value;
    trees that are higher on the right than the left should return a negative value;
    an ideally-balanced tree should return 0.
in_order(self): Return a generator that returns each node value from in-order traversal.
pre_order(self): Return a generator that returns each node value from pre-order traversal.
post_order(self): Return a generator that returns each node value from post_order traversal.
breadth_first(self): Return a generator returns each node value from breadth-first traversal.

"""

from queue import Queue


class Node():
    """Node object for the binary search tree."""

    def __init__(self, value, left=None, right=None, parent=None):
        """Instantiate a node object."""
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


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
                    current_node.left.parent = current_node
                    self._size += 1
                    break
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    current_node.right.parent = current_node
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

    def balance(self, node=self.root):
        """Return numerical representation of how balanced the tree (or branches) is."""
        if node.left:
            depth_left = self.depth(node.left) + 1
        else:
            depth_left = 0
        if node.right:
            depth_right = self.depth(node.right) + 1
        else:
            depth_right = 0
        balance = depth_right - depth_left
        return balance

    def in_order(self):
        """Return generator that returns tree values one at a time using in-order traversal."""
        stack = []
        current_node = self.root
        while len(stack) or current_node is not None:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                yield current_node
                current_node = current_node.right

    def pre_order(self):
        """Return generator that returns tree values one at a time using pre-order traversal."""
        stack = []
        current_node = self.root
        if current_node is None:
            return
        stack.append(current_node)
        while len(stack):
            current_node = stack.pop()
            yield current_node
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    def post_order(self):
        """Return a generator that yields tree values according to the post order."""
        current_node = self.root
        stack = []
        last_node_vis = None
        while len(stack) or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_node_vis != peek_node.right:
                    current_node = peek_node.right
                else:
                    yield peek_node
                    last_node_vis = stack.pop()

    def breadth_first(self):
        """Return a generator that yields tree values according to breadth first traversal."""
        trav_list = Queue([self.root])
        while trav_list.peek():
            current_node = trav_list.dequeue()
            if current_node.left:
                trav_list.enqueue(current_node.left)
            if current_node.right:
                trav_list.enqueue(current_node.right)
            yield current_node

    def delete(self, value):
        """Get rid of a node. Or at least its connection."""
        target_node = self.search(value)
        if not target_node:
            return
        if not (target_node.left or target_node.right):
            if target_node.value > target_node.parent.value:
                target_node.parent.right = None
            else:
                target_node.parent.left = None
        elif not (target_node.left and target_node.right):
            if target_node.left:
                target_node.left.parent = target_node.parent
                target_node.parent.left = target_node.left
            else:
                target_node.right.parent = target_node.parent
                target_node.parent.right = target_node.right
        else:
            current_node = target_node.right
            while current_node.left:
                current_node = current_node.left
            replace_node = current_node
            self.delete(current_node.value)
            self._size += 1  # undoes size change within delete
            if target_node.parent:
                replace_node.parent = target_node.parent
                if replace_node.value < target_node.value:
                    target_node.parent.left = replace_node
                else:
                    target_node.parent.right = replace_node
            replace_node.left = target_node.left
            replace_node.right = target_node.right
        target_node.parent = None
        target_node.left = None
        target_node.right = None
        self._size -= 1
