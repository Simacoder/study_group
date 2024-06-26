# ------------ nested Vertex class ----
class Vertex:
    """ Lightweight vetex structure for a graph.  """
    __slots__ = '_element'
    
    def __init__(self, x):
        """ Do not call constructor directly . Use Graph insert_vert() """
        self._element = x

    def element(self):
        """ Return elemnet associated with this vertex. """
        return self._element
    
    def __hash__(self):
        """ All the vertex  to be map / key """
        return hash(id(self))
    

# ---------- nested Edge Class ----
class Edge:
    """ Lightweight edge for structure  """
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """ do not call constructor direclty  """
        self._origin = u
        self._destination = v 
        self._element = x

    def endpoints(self):
        """ Return (u,v) tuple for vertices u and v """
        return (self._origin, self._destination)
    
    def opposite(self, v):
        """ Return the vertex that is opposite v on the side """
        return self._destination if v is self._origin else self._origin
    
    def element(self):
        """ Return elememnt associated with this edge"""
        return self._element
    
    def __hash__(self):   # allow the ede to map /set key 
        return hash((self._origin, self._destination))
    
    
