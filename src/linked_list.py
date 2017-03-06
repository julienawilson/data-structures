"""Implementation of Linked_List data type."""


class LinkedList(object):
    """Class representation of linked list."""

    def __init__(self, iterable=None):
        """Instantiate linked list."""
        self.head_node = None
        self.length = 0
        try:
            for item in iterable:
                self.push(item)
        except TypeError:
            if iterable:
                return "Please only enter iterable values"

    def push(self, contents):
        """Add node to this linked list."""
        self.head_node = Node(contents, self.head_node)
        self.length += 1

    def pop(self):
        """Remove and return the current head node."""
        if not self.head_node:
            return "Linked list is already empty"
        old_head_node = self.head_node
        self.head_node = self.head_node.next_node
        self.length -= 1
        return old_head_node.contents

    def size(self):
        """Return the current size of this linked list."""
        return self.length

    def search(self, search_value):
        """Return the node with the searched contents if found."""
        if self.length:
            if search_value == self.head_node.contents:
                return self.head_node
            current_node = self.head_node
            while current_node.contents != search_value:
                if current_node.next_node is None:
                    return None
                current_node = current_node.next_node
            return current_node
        else:
            return None

    def remove(self, remove_node):
        """Remove a node from linked list."""
        if not self.length:
            raise ValueError("This list is empty")
        if remove_node == self.head_node:
            self.head_node = self.head_node.next_node
            self.length -= 1
            return None
        elif remove_node is None:
            raise ValueError("Provided value not in list.")
        current_node = self.head_node
        while True:
            if current_node.next_node == remove_node:
                break
            if current_node.next_node is None:
                raise ValueError("Provided value not in list.")
            current_node = current_node.next_node
        try:
            current_node.next_node = current_node.next_node.next_node
        except AttributeError:
            pass
        self.length -= 1

    def display(self):
        """Return the tuple of all values in linked list."""
        if self.length == 0:
            return None
        else:
            new_list = [self.head_node.contents]
            current_node = self.head_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
                new_list.append(current_node.contents)
            return tuple(new_list)


class Node(object):
    """Class representation of linked list node."""

    def __init__(self, contents, next_node):
        """Instantiate linked list node."""
        self.contents = contents
        self.next_node = next_node