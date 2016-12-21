"""Priority Queue data structure."""


class PriorityQueue(object):
    """Priority Queue data structure.

    .insert(item) - adds an item to the queue and sorts
    .pop() - removes the highest priority item, returns its value.
    .peek() - returns the value of the highest priority item.
    """

    def __init__(self, iterable=None):
        """Initialize the Priority Queue."""
        self._pq_list = []
        if hasattr(iterable, "__iter__"):
            self.bin_list = [i for i in iterable]
            self._sort()

    def _sort(self):
        """Sort the priority queue first by priority, then longest residency."""
        prio_nums = list(set([item[0] for item in self._pq_list]))
        result = []
        for priority in prio_nums:
            this_list = [item for item in self._pq_list if item[0] == priority]
            result += this_list
        return result
