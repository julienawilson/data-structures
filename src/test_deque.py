"""Tests for Deque."""
import pytest


@pytest.fixture()
def empty_deque():
    """Build a sample deque for testing."""
    from deque import Deque
    empty_deque = Deque()
    return empty_deque


@pytest.fixture()
def full_deque():
    """Build a sample deque for testing."""
    from deque import Deque
    full_deque = Deque([1, 2, 3])
    return full_deque


def test_deque_empty_init(empty_deque):
    """Test for empty deque init."""
    assert empty_deque.head_node is None
    assert empty_deque.tail_node is None


def test_deque_append(empty_deque):
    """Test for append on deque."""
    empty_deque.append("First append")
    assert empty_deque.head_node.contents == "First append"
    assert empty_deque.tail_node.contents == "First append"


def test_deque_append_full(full_deque):
    """Test for append on deque."""
    full_deque.append("Last append")
    assert full_deque.head_node.contents == 3
    assert full_deque.tail_node.contents == "Last append"


def test_deque_append_left(empty_deque):
    """Test for append left on deque."""
    empty_deque.append_left("First append")
    assert empty_deque.head_node.contents == "First append"
    assert empty_deque.tail_node.contents == "First append"


def test_deque_append_left_full(full_deque):
    """Test for append left on deque."""
    full_deque.append_left("Last append")
    assert full_deque.head_node.contents == "Last append"
    assert full_deque.tail_node.contents == 1


def test_pop_empty(empty_deque):
    """Test for pop left on empty deque."""
    with pytest.raises(ValueError):
        empty_deque.pop()


def test_pop_full(full_deque):
    """Test for pop left on deque."""
    assert full_deque.pop() == 1


def test_pop_empty_left(empty_deque):
    """Test for pop left on empty deque."""
    with pytest.raises(ValueError):
        empty_deque.pop_left()


def test_pop_full_left(full_deque):
    """Test for pop left on deque."""
    assert full_deque.pop_left() == 3


def test_peek_empty(empty_deque):
    """Test for peek left on empty deque."""
    assert empty_deque.peek() is None


def test_peek_full(full_deque):
    """Test for peek left on deque."""
    assert full_deque.peek() == 1


def test_peek_empty_left(empty_deque):
    """Test for peek left on empty deque."""
    assert empty_deque.peek_left() is None


def test_peek_full_left(full_deque):
    """Test for peek left on deque."""
    assert full_deque.peek_left() == 3
