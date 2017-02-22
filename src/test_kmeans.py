import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def kmc():
    """Fixture to return a default KMC."""
    from k_means import KMeansClassifier
    return KMeansClassifier()


@pytest.fixture
def some_data():
    """Fixture to return some dummy data."""
    data = np.array([[2,3],[4,5],[6,7],[8,9],[1,1],[2,2],[3,3],[4,4]])
    return pd.DataFrame(data=data)


def test_find_mean(kmc, some_data):
    """Unit test for find mean."""
    data_means = kmc._find_mean(some_data)
    assert data_means == [3.75, 4.25]


def test_calc_distance(kmc):
    """Test distance calculator helper method."""
    assert kmc._calc_distance([0, 0, 0, 0], [3, 4, 0, 0]) == 5.0
