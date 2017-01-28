"""Test for our implemtation of Trie Tree."""

import pytest


@pytest.fixture()
def empty_trie():
    """Build a sample trie for testing."""
    from trie import TrieTree
    empty_trie = TrieTree()
    return empty_trie


def test_trie_has_root(empty_trie):
    """Test that an empty trie has a root of *."""
    assert empty_trie.root == '*'


def test_empty_trie_trie_size_zero(empty_trie):
    """Test that an empty trie has a size of zero."""
    assert empty_trie.size == 0


def test_insert_trie_increases_size(empty_trie):
    """Test insertion increases the size by one."""
    empty_trie.insert('table')
    assert empty_trie.size == 1


def test_contains_false(empty_trie):
    """Test that contains() returns false on empty trie."""
    assert not empty_trie.contains('table')


def test_insert_makes_word_contains_true(empty_trie):
    """Test that contains returns true after inserting same word."""
    empty_trie.insert('maelstrom')
    assert empty_trie.contins('maelstrom')
