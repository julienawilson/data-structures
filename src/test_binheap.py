"""Tests for building a binary test."""

import pytest


@pytest.fixture()
def empty_heap():
    """Fixture for easy creation of an empty heap."""
    from binheap import Binheap
    return Binheap()


@pytest.fixture()
def full_heap():
    """Fixture for easy creation of a populated heap."""
    from binheap import Binheap
    return Binheap([1, 3, 4, 5, 6, 7, 8, 9])


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


def test_full_push(empty_heap):
    """Test that push adds values to a populated list and sorts."""
    full_heap.push(2)
    assert full_heap.bin_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
