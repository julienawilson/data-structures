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
        if priority not in self._pq_dict.keys():
            self._pq_dict[priority] = []
        self._pq_dict[priority].append(value)

    def pop(self):
        """Remove the highest priority item, returns its value."""
        pop_val = self.peek()
        hi_pri = sorted(self._pq_dict.keys())[0]
        if len(self._pq_dict[hi_pri]) == 1:
            del self._pq_dict[hi_pri]
        else:
            self._pq_dict[hi_pri] = self._pq_dict[hi_pri][1:]
        return pop_val

    def peek(self):
        if len(self._pq_dict.keys()) == 0:
            raise KeyError("The Priority Queue is empty.")
        hi_pri = sorted(self._pq_dict.keys())[0]
        pop_val = self._pq_dict[hi_pri][0]
        return pop_val
