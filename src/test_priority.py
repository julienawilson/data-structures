"""Test the priority queue's functionality."""


import pytest

INPUT_VALUES = []


@pytest.fixture(scope="method", params=INPUT_VALUES)
def pri(request):
    """Paramaterized fixture for testing."""
    from priority import PriorityQueue
    return PriorityQueue(request.param)
