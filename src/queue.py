"""Implementation of Queue."""

from dll import DoublyLinkedList


class Queue(object):
    """Class implementation of queue.

    1.  Enqueue: Add new head node.
    2.  Dequeue: Remove and return tail node value.
    3.  Peek: Display tail node,
    4.  Size: Display queue length.

    """

    def __init__(self, iterable=None):
        """Instatiate Queue."""
        self.dll = DoublyLinkedList(iterable)

    def enqueue(self, contents):
        """Add new head node."""
        self.dll.push(contents)

    def dequeue(self):
        """Remove and return last node value."""
        try:
            old_tail_node_contents = self.dll.shift()
            return old_tail_node_contents
        except IndexError:
            raise IndexError('Queue is already empty.')

    def peek(self):
        """Display but don't remove the contents of tail node."""
        try:
            return self.dll.tail_node.contents
        except AttributeError:
            return None

    def size(self):
        """Return Queue length."""
        return self.dll.length
