"""Tests for dll.py."""

import pytest


@pytest.fixture
def sample_dll():
    """Create testing dlls."""
    from dll import DoublyLinkedList
    one_dll = DoublyLinkedList([1])
    empty_dll = DoublyLinkedList()
    new_dll = DoublyLinkedList([1, 2, 3, 4, 5])
    return one_dll, empty_dll, new_dll


def test_node_init():
    """Test node class init."""
    from dll import Node
    new_node = Node(0, None, None)
    assert new_node.contents == 0
    assert new_node.next_node is None
    assert new_node.previous_node is None


def test_dll_init():
    """Test for dll init."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    assert empty_dll.length == 0
    assert empty_dll.head_node is None
    assert empty_dll.tail_node is None


def test_dll_push():
    """Test for dll push."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    new_dll.push("new")
    assert new_dll.length == 6
    assert new_dll.head_node.contents == "new"
    empty_dll.push("second")
    assert empty_dll.length == 1
    assert empty_dll.head_node.contents == "second"


def test_dll_append():
    """Test for dll push."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    empty_dll.append("new")
    assert empty_dll.length == 1
    assert empty_dll.tail_node.contents == "new"
    assert empty_dll.head_node.contents == "new"
    new_dll.append("second")
    assert new_dll.length == 6
    assert new_dll.tail_node.contents == "second"
    one_dll.append('2')
    assert one_dll.length == 2
    assert one_dll.tail_node.contents == '2'
    assert one_dll.head_node.contents == 1


def test_dll_pop():
    """Test for dll pop."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    assert new_dll.pop() == 5
    assert new_dll.length == 4
    assert one_dll.pop() == 1
    assert one_dll.length == 0


def test_dll_shift():
    """Test for dll shift."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    assert new_dll.shift() == 1
    with pytest.raises(IndexError):
        assert empty_dll.shift()
    assert one_dll.shift() == 1
    assert one_dll.length == 0


def test_dll_remove():
    """Test for dll remove."""
    from dll import DoublyLinkedList
    one_dll, empty_dll, new_dll = sample_dll()
    new_dll.remove(3)
    assert new_dll.length == 4
    assert new_dll.head_node.next_node.next_node.contents == 2
    assert new_dll.head_node.next_node.next_node.previous_node.contents == 4
    try:
        new_dll.remove(10)
    except NameError:
        assert True
    new_dll.remove(5)
    assert new_dll.head_node.contents == 4
    new_dll.remove(1)
    assert new_dll.tail_node.contents == 2
    empty_dll = DoublyLinkedList()
    try:
        empty_dll.remove(100)
    except NameError:
        assert True
    one_dll = DoublyLinkedList([1])
    one_dll.remove(1)
    assert one_dll.head_node is None
    assert one_dll.tail_node is None
    assert one_dll.length == 0
