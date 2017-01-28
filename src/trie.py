"""This module is an implementation of a trie tree.

Words branch out from root, with root's immediate children being
the initial letter of each word. Words can then branch from that initial,
as well as from initial substrings.

Methods include:
contains(word): Check to see whether a word is in the tree.
insert(word): Inserts a word into the trie tree.
"""


class Node(object):
    """A class for the tree's nodes."""

    def __init__(self, value):
        """Instantiate a node in the tree."""
        if value.isalpha():
            value = value.lower()
            self.children = {}


class TrieTree(object):
    """A class for trie trees."""

    def __init__(self):
        """Instantiate an empty trie tree."""
        self.root = Node("*")
        self.size = 0

    def contains(self, word):
        """Check whether a word is in the trie tree."""
        this_node = self.root
        word += "$"
        for letter in word:
            if letter in this_node.children:
                this_node = this_node.children[letter]
                if this_node == "$":
                    return True
            return False

    def insert(self, word):
        """Insert a word into the trie tree."""
        this_node = self.root
        if self.contains(word):
            return
        word += "$"
        for letter in word:
            if letter in this_node.children:
                this_node = this_node.chilren[letter]
            else:
                this_node.children[letter] = Node(letter)
        self.size += 1
