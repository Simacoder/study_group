
from stack_test import ArrayStack 

def is_match(expr):
    """ Return true if all delimeters are properly match; false otherwise. """

    lefty = '({['
    righty = ')}]'

    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

print(is_match('[(5+x)-(y+z)]'))