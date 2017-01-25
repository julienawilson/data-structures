"""Class for hash tables.

Choices for hashing algorithms are additive hash and xor hash. 
Additive hash sums the Unicode code point for each letter in the word or string, 
then calls modulo with the number of buckets in the table.
XOR hash runs exclusive or with the letters of the word or string.
Methods include:
set(key, value): Add a key-value pair to the hash table.
get(key): Retrieve a value for the given key.

"""



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
        if hash_alg == 'xor':
            return self._xor_hash
        else:
            raise ValueError("Please enter a valid hash algorithm.  The options are 'additive' and 'xor'.")

    def _additive_hash(self, word):
        """Return Additive hash value."""
        return sum([ord(char) for char in list(word)]) % self._size

    def _xor_hash(self, word):
        """Return a xor hash."""
        hash_val = 0
        for i in range(len(word)):
            hash_val ^= ord(word[i])
        return hash_val

    def set(self, key, value):
        """Set a new key-value pair in the hash table."""
        if type(key) is not str:
            raise TypeError("Key for hash table must be a string.")
        hash_val = self._hash_alg(key)
        for pair in self.buckets[hash_val]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[hash_val].append([key, value])

    def get(self, key):
        """Get the value from the hash table."""
        if type(key) is not str:
            raise TypeError("Key for hash table must be a string.")
        hash_val = self._hash_alg(key)
        for pair in self.buckets[hash_val]:
            if pair[0] == key:
                return pair[1]
        return
