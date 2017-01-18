"""Implement a double queue, accessable at head and tail."""

from dll import DoublyLinkedList


class Deque(object):
    """Using a doubly-linked list to build a deque."""

    def __init__(self, iterable=None):
        """Initialize the deque."""
        self.dll = DoublyLinkedList(iterable)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node

    def append(self, contents):
        """Add node to this dll."""
        self.dll.append(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node

    def append_left(self, contents):
        """Add a node to the left side of this dll."""
        self.dll.push(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node

    def pop_left(self):
        """Pop a node from the left side of this dll."""
        popped = self.dll.pop()
        if popped is None:
            raise ValueError
        self.head_node = self.dll.head_node
        return popped

    def pop(self):
        """Pop a node from the right side of this dll."""
        popped = self.dll.shift()
        if popped is None:
            raise ValueError
        self.tail_node = self.dll.tail_node
        return popped

    def peek(self):
        """Look at the tail of the dll."""
        if self.dll.length == 0:
            return None
        return self.dll.tail_node.contents

    def peek_left(self):
        """Look at the head of the dll."""
        if self.dll.length == 0:
            return None
        return self.dll.head_node.contents

    def size(self):
        """Report the length of the queue."""
        return self.dll.length
