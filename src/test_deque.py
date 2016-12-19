"""Tests for Deque."""
import pytest


@pytest.fixture
def empty_deque():
    """Build a sample deque for testing."""
    from deque import Deque
    empty_deque = Deque()
    return empty_deque


@pytest.fixture
def full_deque():
    """Build a sample deque for testing."""
    from deque import Deque
    full_deque = Deque([1, 2, 3])
    return full_deque


def test_deque_empty_init(empty_deque):
    """Test for empty deque init."""
    empty_deque = empty_deque()
    assert empty_deque.head_node is None
    assert empty_deque.tail_node is None


def test_deque_append(empty_deque):
    """Test for append on deque."""
    empty_deque = empty_deque()
    empty_deque.append("First append")
    assert empty_deque.head_node.contents == "First append"
    assert empty_deque.tail_node.contents == "First append"


def test_deque_append_full(full_deque):
    """Test for append on deque."""
    full_deque = full_deque()
    full_deque.append("Last append")
    assert full_deque.head_node.contents == 3
    assert full_deque.tail_node.contents == "Last append"


def test_deque_append_left(empty_deque):
    """Test for append left on deque."""
    empty_deque = empty_deque()
    empty_deque.append_left("First append")
    assert empty_deque.head_node.contents == "First append"
    assert empty_deque.tail_node.contents == "First append"


def test_deque_append_left_full(full_deque):
    """Test for append on deque."""
    full_deque = full_deque()
    full_deque.append("Last append")
    assert full_deque.head_node.contents == "Last append"
    assert full_deque.tail_node.contents == 1
