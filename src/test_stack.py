"""Tests for stack.py."""

import pytest


@pytest.fixture
def sample_stack():
    """Create testing stacks."""
    from stack import Stack
    one_stack = Stack([1])
    empty_stack = Stack()
    new_stack = Stack([1, 2, 3, 4, 5])
    return one_stack, empty_stack, new_stack


def test_stack_empty_length():
    """Test for empty stack length."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert empty_stack.length == 0


def test_stack_empty_head_node():
    """Test for empty stack head node."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert empty_stack.head_node is None


def test_stack_new_length():
    """Test for new stack length."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert new_stack.length == 5


def test_stack_new_contents():
    """Test for new stack head node contents."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert new_stack.head_node.contents == 5


def test_stack_new_push():
    """Test for new stack head node contents."""
    one_stack, empty_stack, new_stack = sample_stack()
    new_stack.push(34)
    assert new_stack.head_node.contents == 34


def test_stack_one_push():
    """Test for new stack head node contents."""
    one_stack, empty_stack, new_stack = sample_stack()
    one_stack.push(34)
    assert one_stack.head_node.contents == 34


def test_stack_empty_push():
    """Test for empty stack head node contents."""
    one_stack, empty_stack, new_stack = sample_stack()
    empty_stack.push(34)
    assert empty_stack.head_node.contents == 34


def test_stack_new_pop():
    """Test that pop the new stack returns 5."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert new_stack.pop() == 5


def test_stack_new_pop_length():
    """Test that pop the new stack decreases length."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert new_stack.pop() == 5


def test_stack_one_pop():
    """Test that pop of one stack returns 1."""
    one_stack, empty_stack, new_stack = sample_stack()
    assert one_stack.pop() == 1


def test_stack_one_pop_contents():
    """Test that pop of one stack behaves as expeted."""
    one_stack, empty_stack, new_stack = sample_stack()
    one_stack.pop()
    assert one_stack.head_node is None


def tst_stack_empty_pop():
    """Test that pop empty stack throws correct error."""
    one_stack, empty_stack, new_stack = sample_stack()
    with pytest.raises(TypeError):
        empty_stack.pop()