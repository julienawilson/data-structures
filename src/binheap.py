"""Binheap Data Structure."""


class Binheap(object):
    """
    Binheap data structure.

    .pop: Removes lowest value and reorders heap.
    .push: Adds a value to the end and reorders heap.
    """

    def __init__(self, iterable=None):
        """Create the Binheap."""
        self.bin_list = []
        if hasattr(iterable, "__iter__"):
            self.bin_list = [i for i in iterable]
