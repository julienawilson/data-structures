"""Priority Queue data structure."""


class PriorityQueue(object):
    """Priority Queue data structure.

    .insert(item) - adds an item to the queue and sorts
    .pop() - removes the highest priority item, returns its value.
    .peek() - returns the value of the highest priority item.
    """

    def __init__(self, iterable=None):
        """Initialize the Priority Queue."""
        self._pq_dict = {}
        if hasattr(iterable, "__iter__"):
            for val in iterable:
                self.insert(val[0], priority=val[1])

    def insert(self, value, priority=0):
        """Insert values and priorities in to priority queue."""
        if not self._pq_dict[priority]:
            self._pq_dict[priority] = []
        self._pq_dict[priority].append(value)
