"""Class for hash tables."""


class HashTable(object):
    """Something something."""

    def __init__(self, size, hash_alg='additive'):
        """Initialize a hash table."""
        self._size = size
        self.buckets = [[] for bucket in range(self._size)]
        self._hash_alg = hash_alg

    # def _hash(self, hash_alg, word):
    #     if
    #     self.word = word
    #     additive = sum([ord(char) for char in list(word)]) % len(buckets)

    def _add_hash(self, word):
        """Return Additive hash value."""
        return sum([ord(char) for char in list(word)]) % self._size


    # def set(self, key, value)