"""Tests for the K-Means Classifier."""

from math import sqrt
import pandas as pd
import pytest
import numpy as np


@pytest.fixture
def kmc():
    """Fixture to return a default KMC."""
    from k_means import KMeansClassifier
    return KMeansClassifier()


@pytest.fixture
def some_data():
    """Fixture to return some dummy data."""
    data = np.array([[2, 3], [4, 5], [6, 7], [8, 9], [1, 1], [2, 2], [3, 3], [4, 4]])
    return pd.DataFrame(data=data)


def test_calc_distance_rows(kmc):
    """Test the _calc_distance method of the K Means Classifier."""
    rows = [[2, 2, 1, 0], [0, 0, 1, 0]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class', 'dummy'])
    assert kmc._calc_distance(data.loc[0], data.loc[1]) == sqrt(8)


def test_find_mean(kmc, some_data):
    """Unit test for find mean."""
    data_means = kmc._find_mean(some_data)
    assert data_means == [3.75, 4.25]


def test_calc_distance(kmc):
    """Test distance calculator helper method."""
    assert kmc._calc_distance([0, 0, 0, 0], [3, 4, 0, 0]) == 5.0


def test_random_centroids(kmc):
    """Test that 2 random centroids chosen given a data set to use."""
    dataset = [[1,2,7,3], [5,4,3,8], [5,3,1,7], [7,2,9,11]]
    assert len(kmc._random_centroids(dataset, 2)) == 2
    assert len(kmc._random_centroids(dataset, 2)[0]) == 2
    assert len(kmc._random_centroids(dataset, 2)[1]) == 2
