from collections.abc import MutableMapping


class UnsortedTableMap(MutableMapping):
    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for k, v in self._table:
            if k == key:
                return v
        raise KeyError('Key Error: ' + repr(key))

    def __setitem__(self, key, value):
        for item in self._table:
            if item[0] == key:
                item[1] = value
                return
        self._table.append([key, value])

    def __delitem__(self, key):
        for j in range(len(self._table)):
            if self._table[j][0] == key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(key))

    def __iter__(self):
        for key, value in self._table:
            yield key

    def __len__(self):
        return len(self._table)

    def items(self):
        return [(key, value) for key, value in self._table]

# Example usage
mymap = UnsortedTableMap()
mymap['a'] = 1
mymap['b'] = 2

print(mymap.items())  # Output: [('a', 1), ('b', 2)]


"""
Explanation
Initialization (__init__): Creates an empty list _table to store key-value pairs.
__getitem__: Iterates through the list _table to find the value associated with the given key.
__setitem__: Checks if the key exists and updates its value; otherwise, appends a new key-value pair to the list.
__delitem__: Finds the key in the list and removes the corresponding key-value pair.
__iter__: Yields each key in the _table list.
__len__: Returns the length of the _table list.
items Method Implementation
List Comprehension: The list comprehension [(key, value) for key, value in self._table] iterates over each key-value pair in _table.
Return a List of Tuples: It constructs and returns a list of (key, value) tuples.
Running Time
The running time of the items() method in this implementation is 
𝑂(𝑛)
O(n):

The list comprehension iterates over all 𝑛
n elements in _table, collecting them into a new list.
Each iteration step takes constant time 
𝑂(1)
O(1).
Therefore, the total time complexity is 
𝑂(𝑛)
O(n).
This implementation ensures that the items() method runs in linear time with respect to the number of key-value pairs in the UnsortedTableMap.

"""