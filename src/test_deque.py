"""Tests for Deque."""


def test_deque_empty_init():
    """Test for empty deque init."""
    from deque import Deque
    empty_deque = Deque()
    assert empty_deque.length == 0
    assert empty_deque.head_node is None
    assert empty_deque.tail_node is None
    # assert empty_deque.size() == 0


def test_deque_append():
    """Test for append on deque."""
    from deque import Deque
    empty_deque = Deque()
    empty_deque.append("First append")
    assert empty_deque.head_node.contents == "First append"
    assert empty_deque.tail_node.contents == "First append"
    # assert empty_deque.size() == 0
