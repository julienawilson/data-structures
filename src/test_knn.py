"""Tests for K-nearest neigbors module."""

import pytest
from knn import KNN
import numpy as np


DATASET = [
    np.array([7.49, 3.16, 5.9, 8.8, 1]),
    np.array([9.00, 1.17, 5.9, 8.8, 1]),
    np.array([7.44, 0.47, 6.9, 8.8, 1]),
    np.array([10.12, 3.23, 7.6, 8.8, 1]),
    np.array([6.66, 0.319, 5.9, 8.8, 1]),
    np.array([2.01, 1.87, 8.8, 3.3, 0]),
    np.array([1.78, 1.17, 9.9, 3.3, 0]),
    np.array([3.67, 2.81, 7.7, 3.3, 0]),
    np.array([3.96, 2.61, 8.8, 3.3, 0]),
    np.array([2.99, 2.20, 1.7, 3.3, 0])
]

CLASSES = [
    [[1, 0, 0, 1, 1], [1]],
    [[0, 1, 1, 0, 0, 1], [0, 1]], [[1, 0, 0, 1, 1, 0], [0, 1]],
    [['versicolor', 'setosa', 'setosa', 'versicolor', 'versicolor', 'setosa'], ['setosa', 'versicolor']],
    [['versicolor', 'setosa', 'versicolor', 'versicolor', 'setosa'], ['versicolor']],
]

@pytest.fixture
def convert_csv(filename):
    data = np.loadtxt(filename,
                      delimiter=',',
                      unpack=True,
                      skiprows=1,
                      usecols=(0, 1, 2, 3, 4))
    return data.transpose()

@pytest.fixture
def flowers():
    """Convert flower csv for tests."""
    return convert_csv('flowers_data.csv')

@pytest.fixture
def knn(flowers):
    """Create a KNN object."""
    return KNN(flowers)


def test_predict_returns_class_label(knn):
    """Should return a 0 or 1."""
    assert knn.predict([x[:-1] for x in DATASET]) in (1, 0)


def test_knn_readjusts_for_class_tie(knn):
    """If k turns up a equal class options, try again with k-1."""
    knn = KNN(DATASET, k=2)
    assert knn.predict([np.array([5.5, 3, 5.7, 4.4])]) in (0, 1)


@pytest.mark.parametrize('k', [-1, 12, 'hotsauce'])
def test_knn_raises_errors_on_invalid_input(k):
    """Test for the errors."""
    with pytest.raises(ValueError):
        KNN(DATASET, k=k)


@pytest.mark.parametrize('classes', CLASSES)
def test_getting_dominant_classes(classes, knn):
    """Should return a list of the dominant class or classes among KNN."""
    assert sorted(knn._get_dominant_class(classes[0])) == classes[1]
