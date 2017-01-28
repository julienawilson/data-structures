"""Test for our implemtation of Trie Tree."""

import pytest


@pytest.fixture()
def empty_trie():
    """Build a sample trie for testing."""
    from trie import TrieTree
    empty_trie = TrieTree()
    return empty_trie


def test_trie_has_root(empty_trie):
    """Test that an empty trie has a root dict."""
    assert empty_trie.root == {}


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
    assert empty_trie.contains('maelstrom')


def test_insert_makes_similar_word_contains_false(empty_trie):
    """Test that contains returns true after inserting same word."""
    empty_trie.insert('maelstrom')
    assert not empty_trie.contains('maelstro')


def test_insert_makes_similar_word_contains_false_again(empty_trie):
    """Test that contains returns true after inserting same word."""
    empty_trie.insert('maelstrom')
    assert not empty_trie.contains('maelstrome')


def test_insert_something_already_there(empty_trie):
    """Test that a trie doesn't grow after inserting same word."""
    empty_trie.insert('golf')
    empty_trie.insert('golf')
    assert empty_trie.size == 1


def test_insert_subword_adds_word(empty_trie):
    """Test that adding a word that is a slice of another word adds it."""
    empty_trie.insert('golf')
    empty_trie.insert('go')
    assert empty_trie.size == 2


def test_insert_subword_searchable(empty_trie):
    """Test that adding a word that is a slice of another word adds it."""
    empty_trie.insert('golf')
    empty_trie.insert('go')
    assert empty_trie.contains('go')


def test_insert_longword(empty_trie):
    """Test that adding a word that is a slice of another word adds it."""
    empty_trie.insert('golf')
    empty_trie.insert('golferhole')
    assert empty_trie.size == 2


def test_insert_longword_searchable(empty_trie):
    """Test that adding a word that is a slice of another word adds it."""
    empty_trie.insert('golf')
    empty_trie.insert('golferhole')
    assert empty_trie.contains('golferhole')


def test_remove_absent_word(empty_trie):
    """Test that removing a nonexistent word raises exception."""
    with pytest.raises(AttributeError):
        empty_trie.remove("gotcha")


def test_remove_truly_removes(empty_trie):
    """Test that remove method deletes a word from the trie tree."""
    empty_trie.insert("ephemeral")
    empty_trie.remove("ephemeral")
    assert empty_trie.contains("ephemeral") is False


def test_remove_short_word_w_shared_root(empty_trie):
    """Test removing a word that has a longer cousin in the tree. So to speak."""
    empty_trie.insert("go")
    empty_trie.insert("golf")
    empty_trie.remove("go")
    assert empty_trie.contains("go") is False


def test_remove_short_word_w_shared_root_keeps_longer_word(empty_trie):
    """Test removing a word that has a longer cousin in the tree keeps long word."""
    empty_trie.insert("go")
    empty_trie.insert("golf")
    empty_trie.remove("go")
    assert empty_trie.contains("golf") is True


def test_remove_word_w_shorter_root_word(empty_trie):
    """Test removing a word that has a shorter cousin in the tree."""
    empty_trie.insert("go")
    empty_trie.insert("golf")
    empty_trie.remove("golf")
    assert empty_trie.contains("golf") is False

def test_remove_word_w_shorter_root_word_keeps_shorter_one(empty_trie):
    """Test that removing a word with a word root also in tree keeps the short word."""
    empty_trie.insert("go")
    empty_trie.insert("golf")
    empty_trie.remove("golf")
    assert empty_trie.contains("go") is True


