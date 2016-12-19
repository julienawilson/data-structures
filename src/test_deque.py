"""Tests for Deque."""


def test_deque_empty_init():
    """Test for empty queue init."""
    from deque import Deque
    empty_deque = Deque()
    assert empty_deque.peek() is None
    assert empty_deque.peekleft() is None
    assert empty_deque.size() == 0
