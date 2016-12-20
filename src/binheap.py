"""Binheap Data Structure."""


class Binheap(object):
    """
    Binheap data structure.

    .pop: Removes lowest value and reorders heap.
    .push: Adds a value to the end and reorders heap.
    """

    def __init__(self, iterable=None, style='min'):
        """Create the Binheap."""
        self.style = style
        self.bin_list = []
        if hasattr(iterable, "__iter__"):
            self.bin_list = [i for i in iterable]
            self.bin_list.sort()

    def push(self, value):
        """Push value to end of list and then run sorting algorithm."""
        self.bin_list.append(value)
        self._sort()

    def pop(self):
        """Pop the value at the head of the heap and re-sort."""
        if self.bin_list == []:
            raise ValueError
        self.bin_list[0], self.bin_list[-1] = self.bin_list[-1], self.bin_list[0]
        pop_val = self.bin_list.pop()
        self._sort()
        return pop_val

    def _sort(self):
        i = 0
        if self.style == 'min':
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
        elif self.style == 'max':
            while i < len(self.bin_list):
                try:
                    if self.bin_list[i] < self.bin_list[2 * i + 1]:
                        self.bin_list[i], self.bin_list[2 * i + 1] = self.bin_list[2 * i + 1], self.bin_list[i]
                        i = 0
                        continue
                    elif self.bin_list[i] < self.bin_list[2 * i + 2]:
                        self.bin_list[i], self.bin_list[2 * i + 2] = self.bin_list[2 * i + 2], self.bin_list[i]
                        i = 0
                        continue
                    i += 1
                except IndexError:
                    break
        else:
            raise NameError
