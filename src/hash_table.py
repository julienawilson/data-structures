"""Class for hash tables."""


class HashTable(object):
    """Something something."""

    def __init__(self, size, hash_alg='additive'):
        """Initialize a hash table."""
        self._size = size
        self.buckets = [[] for bucket in range(self._size)]
        self._hash_alg = self._hash(hash_alg)

    def _hash(self, hash_alg):
        if hash_alg == 'additive':
            return self._additive_hash
        else:
            raise ValueError("Please enter a valid hash algorithm.  The options are 'additive'.")

    def _additive_hash(self, word):
        """Return Additive hash value."""
        return sum([ord(char) for char in list(word)]) % self._size

    def set(self, key, value):
        """Set a new key value pair in the has table."""
        if type(key) is not str:
            raise TypeError("Key for hash table must be a string.")
        hash_val = self._hash_alg(key)
        for pair in self.buckets[hash_val]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[hash_val].append([key, value])
