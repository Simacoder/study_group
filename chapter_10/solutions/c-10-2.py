from collections.abc import MutableMapping

class MyMutableMapping(MutableMapping):
    def __init__(self):
        self._store = {}
    
    def __getitem__(self, key):
        return self._store[key]
    
    def __setitem__(self, key, value):
        self._store[key] = value
    
    def __delitem__(self, key):
        del self._store[key]
    
    def __iter__(self):
        return iter(self._store)
    
    def __len__(self):
        return len(self._store)
    
    def items(self):
        return [(key, self[key]) for key in self]

# Example usage
mymap = MyMutableMapping()
mymap['a'] = 1
mymap['b'] = 2

print(mymap.items())  # Output: [('a', 1), ('b', 2)]

""" 
Explanation
Initialization (__init__): We create an internal dictionary _store to keep the items.
__getitem__: Retrieves the value associated with the given key from the _store dictionary.
__setitem__: Sets the value for the given key in the _store dictionary.
__delitem__: Deletes the key-value pair from the _store dictionary.
__iter__: Returns an iterator over the keys of the _store dictionary.
__len__: Returns the number of items in the _store dictionary.
items Method Implementation
List Comprehension: [key for key in self] iterates over all keys in the mapping.
Key-Value Pairs: For each key, self[key] retrieves its corresponding value.
Return a List of Tuples: The method returns a list of (key, value) tuples.
Running Time for UnsortedTableMap
If we apply this items() method to an UnsortedTableMap subclass, the running time depends on the underlying implementation. Assuming an UnsortedTableMap uses a list to store key-value pairs:

Iteration Over Keys: The iteration over the keys (for key in self) involves traversing the list of keys. This takes 
𝑂(𝑛)
O(n) time where 𝑛
n is the number of items.
Accessing Values: Each self[key] operation may require a linear search through the list, which in the worst case takes 
𝑂(𝑛)
O(n) time per key.
Total Running Time: Since there are 𝑛
n keys and each key lookup is 
𝑂(𝑛)
O(n), the total time complexity is 
𝑂(𝑛)
×
𝑂(𝑛)=𝑂(𝑛2)
O(n)×O(n)=O(n 2).
Thus, the running time of the items() method, if directly applied to the UnsortedTableMap subclass, would be 
𝑂(𝑛2)
O(n2).

"""
