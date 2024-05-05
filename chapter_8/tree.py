class Tree:
    """ Abstract base class representing a tree structure. """

#---------------------- nested position class------------------
    class Position:
        """ An Abstraction representing the location of a single element. """
        
        def element(self):
            """ Return the element stored at this position."""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """ Return true if other position represents the same location. """
            raise NotImplementedError('must be implemented by subclass.')
        
        def __ne__(self, other):
            """ Return true if other does not represent the same location. """
            return not (self == other)
        
#-------------------Abstract methods that concrete subclass must support--------
    def root(self):
        """ Return position representing the tree's root (o None if empty)."""
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        """ Return the position representing p's parents (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        """ Return the number of children that Position p has. """
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        """ Generate an iteration of Positions representing p's children. """
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        """ Return the total number of element in the tree. """
        raise NotImplementedError('must be implemented by subclass')
    

#------ contrete methods implememted in this class ------
    def is_root(self, p):
        """ Return True if Position p represent the root of the tree"""
        return self.root()== p
    
    def is_leaf(self, p):
        """" Return True if position p does not have any children. """
        return self.num_children(p)==0
    
    def is_empty(self):
        """ Return True if the tree is empty. """
        return len(self)== 0
    
    def depth(self, p):
        """ Return the number of of levels separating Position p from root. """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height1(self):
        """ return the height of the tree. """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))