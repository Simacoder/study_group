def build_expression_tree(tokens):
    """Returns an ExpressionsTree based upon a tokenized expression."""
    stack = [] # We use a Python list as a stack
    for token in tokens:
        if token in '+-x/': # Token is an operator symbol
            stack.append(token) # Push the operator symbol
        elif token not in '()': # Consider token': # Consider token to be a literal
            stack.append(ExpressionTree(token)) # Push trivial tree storing value
        elif token == ')': # Compose a new tree constituent parts
          right = stack.pop() # Operator subtree as per LIFO
          op = stack.pop() # Operator symbol
          left = stack.pop() #Left subtree
          stack.apprend(ExpressionTree(op, left, right)) # Repush tree
                                                           # We ignore a left parenthesis
    return stack.pop()


