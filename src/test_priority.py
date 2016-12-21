"""Test the priority queue's functionality."""


import pytest

INPUT_VALUES = [
    ([], {}),
    ([(1, 'a'), (2, 'b'), (3, 'c')], {'1': ['a'], '2': ['b'], '3': ['c']}),
    ([(2, 'a'), (5, 'b'), (12, 'c')], {'2': ['a'], '5': ['b'], '12': ['c']}),
    ([(15, 'words'), (6, 'are'), (70, 'hard')], {'6': ['are'], '15': ['words'], '70': ['hard']}),
    ([(1, 15), (2, 20), (3, 25)], {'1': [15], '2': [20], '3': [25]}),
    ([(1, 'a'), (1, 'b'), (2, 'c')], {'1': ['a', 'b'], '2': ['c']}),
]


@pytest.fixture(scope="module", params=INPUT_VALUES)
def pri(request):
    """Paramaterized fixture for testing."""
    from priority import PriorityQueue
    processed = PriorityQueue(request.param[0])
    prioq = (processed, request.param[1])
    return prioq


def test_init(pri):
    from priority import PriorityQueue
    assert isinstance(pri[0], PriorityQueue)


def test_insert(pri):
    assert pri[0]._pq_dict == pri[1]
    # (the_input, the_expected_output) = pri
