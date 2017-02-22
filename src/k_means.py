"""Implementation of the K-Means Classifier."""
import random

class KMeansClassifier(object):
    """Implementation of the K-Means Classifier."""

    def __init__(self, max_iter=None, min_step=None):
        """Initialize a K-Means Classifier object."""
        self.max_iter = max_iter
        self.min_step = min_step
        self.fitted = False

    def fit(self, data, k=2):
        """Fit K centroids to given data."""
        if k < 0 or k > len(data):
            raise ValueError("K must a positive integer less than the length of data.")

        centriods = randomCentroids(k)

        iteration = 0
        old_centroids = None

        while not _should_stop(old_centroids, centroids, iteration):
            old_centroids = centroids
            iteration += 1

            labels = _classify(data, centroids)

            centroids = _assign_centroids(data, labels, k)

        self.fitted = True
        pass

    def predict(self, data):
        """Predict the class of given test data after fit."""
        if self.fitted == False:
            raise RuntimeError('Run KMeansClassifier.fit before running predict')
        pass

    def _calc_distance(self, pt1, pt2):
        """Calculate the distance between two points."""
        dist = 0.0
        for i in range(len(pt1) - 1):
            dist += (pt1[i] - pt2[i])**2
        return sqrt(dist)

    def _classify(self, data, centroids):
        """Assign each datapoint to the nearest centroid."""
        pass

    def _find_mean(self, points):
        """Find the mean coordinates of points."""
        col_means = []
        for column in points:
            col_means.append(points[column].mean())
        return col_means




    def _assign_centroids(self, data, labels, k):
        """Assign centriod coordinates based on distance to member points."""
        pass

    def _should_stop(self, old_centroids, centroids, iteration):
        """Determine if the fit should stop runnng."""
        pass


        k_list = []
        for i in range(k):
            k_list.append([random.uniform(min(data[column]), max(data[column])) for column in range(len(data))])
