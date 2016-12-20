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
    retrun Binheap([1, 2, 3, 4, 5, 6, 7, 8, 9])
