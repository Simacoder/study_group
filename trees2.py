class ExpressionTree(LinkedBinaryTree):
 """An arithmetic expression tree."""
 def __init__ (self, token, left=None, right=None):
    """Create an expression tree.

 In a single parameter form, token should be a leaf value (e.g., 42 ),
 and the expression tree will have that value at an isolated node.

 In a three-parameter version, token should be an operator,
 and left and right should be existing ExpressionTree instances
 that become the operands for the binary operator.
 """
  super().__init__() # LinkedBinaryTree initialization
 if not isinstance(token, str):
 raise TypeError( Token must be a string )
 self. add root(token) # use inherited, nonpublic method
 if left is not None: # presumably three-parameter form
 if token not in +-*x/ :
 raise ValueError( token must be valid operator )
 self. attach(self.root( ), left, right) # use inherited, nonpublic method

 def str (self):
 ”””Return string representation of the expression.”””
 pieces = [ ] # sequence of piecewise strings to compose
 self. parenthesize recur(self.root( ), pieces)
 return .join(pieces)

 def parenthesize recur(self, p, result):
 ”””Append piecewise representation of p s subtree to resulting list.”””
 if self.is leaf(p):
 result.append(str(p.element( ))) # leaf value as a string
 else:
 result.append( ( ) # opening parenthesis
 self. parenthesize recur(self.left(p), result) # left subtree
 result.append(p.element( )) # operator
 self. parenthesize recur(self.right(p), result) # right subtree
 result.append( ) ) # closing parenthesis
                      