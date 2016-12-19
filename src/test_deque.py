"""Tests for Deque."""


def test_deque_empty_init():
    """Test for empty queue init."""
    from deque import Deque
    empty_deque = Deque()
    assert empty_deque.length == 0
    assert empty_deque.head_node is None
    assert empty_deque.tail_node is None
    # assert empty_deque.size() == 0
