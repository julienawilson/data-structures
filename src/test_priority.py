"""Test the priority queue's functionality."""


import pytest

INPUT_VALUES = [
    ([], {}, None, None),
    ([(1, 'a'), (2, 'b'), (3, 'c')], {1: ['a'], 2: ['b'], 3: ['c']}, 'a', 1),
    ([(2, 'a'), (5, 'b'), (12, 'c')], {2: ['a'], 5: ['b'], 12: ['c']}, 'a', 2),
    ([(15, 'words'), (6, 'are'), (70, 'hard')], {6: ['are'], 15: ['words'], 70: ['hard']}, 'are', 6),
    ([(1, 15), (2, 20), (3, 25)], {1: [15], 2: [20], 3: [25]}, 15, 1),
    ([(1, 'a'), (1, 'b'), (2, 'c')], {1: ['a', 'b'], 2: ['c']}, 'a', 1),
]


@pytest.fixture(scope="module", params=INPUT_VALUES)
def pri(request):
    """Paramaterized fixture for testing."""
    from priority import PriorityQueue
    processed = PriorityQueue(request.param[0])
    prioq = (processed, request.param[1], request.param[2], request.param[3])
    return prioq


def test_init(pri):
    """Test that the class initializes."""
    from priority import PriorityQueue
    assert isinstance(pri[0], PriorityQueue)


def test_insert(pri):
    """Test that values are inserted at the right priority in the right order."""
    assert pri[0]._pq_dict == pri[1]
    # (the_input, the_expected_output) = pri


def test_pop(pri):
    """Test that pop returns the right value."""
    try:
        assert pri[0].pop() == pri[2]
    except KeyError:
        assert True


def test_del(pri):
    """Test that empty keys are deleted."""
    try:
        pri[0].pop()
        pri[0].pop()
        assert pri[3] not in pri[0]._pq_dict
    except KeyError:
        assert True


def test_pop_remove(pri):
    """Test that pop properly removes values."""
    try:
        pri[0].pop()
        assert pri[2] not in pri[0]._pq_dict[pri[3]]
    except KeyError:
        assert True


def test_peek(pri):
    """Test that peek returns the right value."""
    try:
        assert pri[0].peek() == pri[2]
    except KeyError:
        assert True
