"""Class for hash tables."""

class HashTable(buckets, hash=additive):
    """Something something."""
    def __init__(self):
        self.bins = [dict for bucket in range(buckets)]

    def _hash(self, additive, word):
        self.additive = additive
        self.word = word

        additive = sum([ord(char) for char in list(word)]) % len(buckets)




