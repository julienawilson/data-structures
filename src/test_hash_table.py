"""Test for our implemtation of hash tables."""

import pytest
# import os
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


def test_set_add_word():
    """Test that set() adds key-value pair."""
    h_table = HashTable(10)
    h_table.set('thinking', 'tiring')
    assert h_table.get('thinking') == 'tiring'


def test_get():
    """Test that get() retrieves value."""
    h_table = HashTable(10)
    h_table.set('thinking', 'tiring')
    assert h_table.get('thinking') == 'tiring'

def test_dictionary_attacks_me_test():
    """Dictionary test."""
    h_table = HashTable(3000)
    f = open("/usr/share/dict/words", 'r')
    while True:
        word = f.readline()
        if not word:
            break
        h_table.set(word, word)
    f_again = open("/usr/share/dict/words", 'r')
    while True:
        word = f_again.readline()
        if not word:
            break
        if word != h_table.get(word):
            assert False
    assert True

def test_dictionary_attacks_me_with_fail():
    """Add a whole dictionary, change a key's value, test the changed happened."""
    not_matching = 0
    h_table = HashTable(3000)
    f = open("/usr/share/dict/words", 'r')
    while True:
        word = f.readline()
        if not word:
            break
        h_table.set(word, word)
    h_table.set("Adirondack\n", "pickle")
    f_again = open("/usr/share/dict/words", 'r')
    while True:
        word = f_again.readline()
        if not word:
            break
        if word != h_table.get(word):
            not_matching += 1
    assert not_matching == 1

