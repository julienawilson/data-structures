"""Test the priority queue's functionality."""


import pytest

INPUT_VALUES = [
    ([], [])
    ([(1, 'a'), (2, 'b'), (3, 'c')], [(1, 'a'), (2, 'b'), (3, 'c')])
    ([(2, 'a'), (5, 'b'), (12, 'c')], [(2, 'a'), (5, 'b'), (12, 'c')])
    ([(15, 'words'), (6, 'are'), (70, 'hard')], [(6, 'are'), (15, 'words'), (70, 'hard')])
    ([(1, 15), (2, 20), (3, 25)], [(1, 15), (2, 20), (3, 25)])
]


@pytest.fixture(scope="method", params=INPUT_VALUES)
def pri(request):
    """Paramaterized fixture for testing."""
    from priority import PriorityQueue
    prioq = (PriorityQueue(request.param[0]), request.param[1])
    return prioq


def test_init(pri):
    from priority import PriorityQueue
    assert isinstance(pri[0], PriorityQueue)


def test_sort(pri):
    assert pri[0] == pri[1]
    # (the_input, the_expected_output) = pri
