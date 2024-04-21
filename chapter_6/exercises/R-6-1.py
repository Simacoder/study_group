""" What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop(). """

class Empty(Exception):
    pass

class ArrayStack:
    """ LIFO stack implementation using python list as underlying storage. """

    def __init__(self):
        self._data =[]

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    x = ArrayStack() # run on jupyter 

    x.push(5)
    x.push(3)
    x.pop()
    x.push(2)
    x.push(8)
    x.pop()
    x.pop()
    x.push(9)
    x.push(1)
    x.pop()
    x.push(7)
    x.push(6)
    x.pop()
    x.pop()
    x.push(4)
    x.pop()
    x.pop()
