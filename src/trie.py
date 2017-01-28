"""This module is an implementation of a trie tree.

Words branch out from root, with root's immediate children being
the initial letter of each word. Words can then branch from that initial,
as well as from initial substrings.

Methods include:
contains(word): Check to see whether a word is in the tree.
insert(word): Inserts a word into the trie tree.
# """


# class Node(object):
#     """A class for the tree's nodes."""

#     def __init__(self, value):
#         """Instantiate a node in the tree."""
#         if value.isalpha() or value in ['$', '*']:
#             value = value.lower()
#             self.children = {}
#             self.value = value
#         else:
#             raise ValueError('That value is not acceptable.')


class TrieTree(object):
    """A class for trie trees."""

    def __init__(self):
        """Instantiate an empty trie tree."""
        self.root = {}
        self.size = 0

    def contains(self, word):
        """Check whether a word is in the trie tree."""
        this_node = self.root
        for letter in word:
            if letter in this_node:
                this_node = this_node[letter]
            else:
                return False
        if '$' in this_node:
            return True
        return False

    def insert(self, word):
        """Insert a word into the trie tree."""
        this_node = self.root
        if self.contains(word):
            return
        word += "$"
        for letter in word:
            if letter in this_node:
                this_node = this_node[letter]
            else:
                this_node[letter] = {}
                this_node = this_node[letter]
        self.size += 1

    def remove(self, word):
        """Remove a word from the trie."""
        if not self.contains(word):
            return
        word += "$"
        self.bubble_down(word, self.root, 0)

    def bubble_down(self, word, node_dict, idx):
        """Search for end of a word and delete it."""
        next_letter = word[idx]
        if next_letter != '$':
            if next_letter in node_dict:
                node_dict = node_dict[next_letter]
                self.bubble_down(word, node_dict, idx + 1)
        if len(node_dict) > 1:
            del node_dict[next_letter]
            return
