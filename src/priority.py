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
                self.insert(val[1], priority=val[0])

    def insert(self, value, priority=0):
        """Insert values and priorities in to priority queue."""
        if str(priority) not in self._pq_dict.keys():
            self._pq_dict[str(priority)] = []
        self._pq_dict[str(priority)].append(value)
