"""Implementation of the K-nearest neighbors classifier.

Categorize new data based on labels of the K closest data points.

There's one public method:
predict(self, new_points, k=None): Takes in a new dataset, and defaults its search
for k neighbors to KNN onject default of 5. Returns the likely class/grouping 
for each set of data in the dataset, based on the k nearest neighbors.
"""
import numpy as np


class KNN(object):
    """K nearest neighbors class."""

    def __init__(self, dataset, k=5):
        """Initialize classifier."""
        if type(k) is not int or k > len(dataset) or k < 0:
            raise ValueError("k must be an integer greater than 0 and less than or equal to length of the dataset")
        self.dataset = dataset
        self.k = 5

    def predict(self, new_points, k=None):
        """Given new data points, predict their classes based on existing data points."""
        if not k:
            k = self.k
        for batch in new_points:
            distance_list = []
            for data_idx in range(len(self.dataset) - 1):
                squares_sum = 0.0
                for item_idx in range(len(batch) - 1):
                    squares_sum += (batch[item_idx] - self.dataset[data_idx][item_idx]) ** 2
                distance_list.append((np.sqrt(squares_sum), self.dataset[data_idx][-1]))
            neighbors = sorted(distance_list)[:k]
            label = self._get_dominant_class([x[1] for x in neighbors])
            if len(label) > 1:
                return self.predict(new_points, k=k - 1)
        return label[0]

    def _get_dominant_class(self, classes):
        """Find, return dominant class of a dataset subset."""
        classes_set = set(classes)
        count = {group: classes.count(group) for group in classes_set}
        highest = max(count.values())
        return [k for k, v in count.items() if v == highest]
