""" Implement a function with signature transfer(S, T) that transfers all elements
from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T. """

#----------R6-3---------------------

class Empty(Exception):
    pass

class Stack():
    def __init__(self):
        self._data = []
         
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, value):
        self._data.append(value)
    
    def top(self):
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans
    
def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())



S,T = Stack(), Stack()

try: S.pop()
except Exception as e: print (e)

for i in range(20):
    S.push(i)
    
print('Top of S is: ', S.top())
transfer(S, T)  
print('Top of T is: ', T.top())
S.full_pop(), T.full_pop()