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
    
    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                return default
            else:
                raise

# Example usage
mymap = MyMutableMapping()
mymap['a'] = 1
mymap['b'] = 2

print(mymap.pop('a'))  # Output: 1
print(mymap.pop('c', 'default'))  # Output: default
try:
    print(mymap.pop('c'))  # Raises KeyError
except KeyError as e:
    print(e)



"""  
Explanation
Initialization (__init__): We create an internal dictionary _store to keep the items.
__getitem__: This method retrieves the value associated with the given key from the _store dictionary.
__setitem__: This method sets the value for the given key in the _store dictionary.
__delitem__: This method deletes the key-value pair from the _store dictionary.
__iter__: This method returns an iterator over the keys of the _store dictionary.
__len__: This method returns the number of items in the _store dictionary.
pop Method Implementation
Attempt to get the value: We use self[key] to get the value associated with key.
Delete the key-value pair: If the key exists, del self[key] removes the key-value pair from the dictionary.
Return the value: The retrieved value is then returned.
Handle KeyError: If the key does not exist, a KeyError is caught. If a default value is provided, it is returned; otherwise, the KeyError is raised again.
This implementation strictly adheres to the use of only the primary abstract methods specified by MutableMapping.

"""
