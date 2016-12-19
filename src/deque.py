"""Implement a double queue, accessable at head and tail."""

from dll import DoublyLinkedList


class Deque(object):
    """Using a doubly-linked list to build a deque."""

    def __init__(self, iterable=None):
        """Initialize the deque."""
        self.dll = DoublyLinkedList(iterable)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length = 0

    def append(self, contents):
        """Add node to this dll."""
        self.dll.append(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length += 1


    # def append_left(self):


    # def pop(self):


    # def pop_left(self):


    # def peek(self):


    # def peek_left(self):


    # def size(self):
