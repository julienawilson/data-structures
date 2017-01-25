"""Test for our implemtation of hash tables."""

import pytest
from hash_table import HashTable

def test_simple_additive_hash():
    """Test that additive hash on small word."""
    h_table = HashTable(10)
    assert h_table._additive_hash('a') == 7

def test_set_add_a_nonstring():
    """Test that set() won't take in a number type."""
    h_table = HashTable(10)
    with pytest.raises(TypeError):
        h_table.set(3, 'AI')

