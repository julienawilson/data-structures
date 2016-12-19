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


    def append_left(self, contents):
        self.dll.push(contents)
        self.head_node = self.dll.head_node
        self.tail_node = self.dll.tail_node
        self.length += 1


    def pop_left(self):
        popped = self.dll.pop()
        if popped is None:
            raise ValueError
        self.head_node = self.dll.head_node
        self.length -= 1
        return popped


    def pop(self):
        popped = self.dll.shift()
        if popped is None:
            raise ValueError
        self.tail_node = self.dll.tail_node
        self.length -= 1
        return popped.


    # def peek(self):


    # def peek_left(self):


    # def size(self):
