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

    def push(self, value):
        """Push value to end of list and then run sorting algorithm."""
        self.bin_list.append(value)
        i = 0
        while i < len(self.bin_list):
            try:
                if self.bin_list[i] > self.bin_list[2 * i + 1]:
                    self.bin_list[i], self.bin_list[2 * i + 1] = self.bin_list[2 * i + 1], self.bin_list[i]
                    i = 0
                    continue
                elif self.bin_list[i] > self.bin_list[2 * i + 2]:
                    self.bin_list[i], self.bin_list[2 * i + 2] = self.bin_list[2 * i + 2], self.bin_list[i]
                    i = 0
                    continue
                i += 1
            except IndexError:
                break
