"""Tests for building a binary test."""

import pytest


@pytest.fixture()
def empty_heap():
    """Fixture for easy creation of an empty heap."""
    from binheap import Binheap
    empty_heap = Binheap()
    return empty_heap


@pytest.fixture()
def full_heap():
    """Fixture for easy creation of a populated heap."""
    from binheap import Binheap
    full_heap = Binheap([1, 3, 4, 5, 6, 7, 8, 9])
    return full_heap


@pytest.fixture()
def max_heap():
    """Fixture for easy creation of a populated heap."""
    from binheap import Binheap
    max_heap = Binheap(iterable=[1, 3, 4, 5, 6, 7, 8, 9], style="max")
    return max_heap


def test_empty_init(empty_heap):
    """Test that the empty heap is initiated."""
    assert empty_heap.bin_list == []


def test_full_init(full_heap):
    """Test that the populated heap is initiated."""
    assert full_heap.bin_list == [1, 3, 4, 5, 6, 7, 8, 9]


def test_empty_push(empty_heap):
    """Test that push adds values to the heap."""
    empty_heap.push(1)
    assert empty_heap.bin_list == [1]


def test_full_push(full_heap):
    """Test that push adds values to a populated list and sorts."""
    full_heap.push(2)
    assert full_heap.bin_list == [1, 2, 4, 3, 6, 7, 8, 9, 5]


def test_full_pop(full_heap):
    """Test .pop() on a full heap."""
    full_heap.pop()
    assert full_heap.bin_list == [3, 5, 4, 9, 6, 7, 8]


def test_empty_pop(empty_heap):
    """Test .pop() on a full heap."""
    with pytest.raises(ValueError):
        empty_heap.pop()


def test_max_init(max_heap):
    """Test init on a max type binheap."""
    assert max_heap.bin_list == [9, 8, 7, 5, 4, 3, 6, 1]
