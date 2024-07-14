#------------------------- nested Vertex class -------------------------
class Vertex:
    """Lightweight vertex structure for a graph."""
    _slots_ = '_element'

    def _init_(self, x):
        """Do not call constructor directly. Use Graph's insert_vertex(x)."""
        self._element = x

    def element(self):
        """Return element associated with this vertex."""
        return self._element

    def _hash_(self):  # will allow vertex to be a map/set key
        return hash(id(self))

#------------------------- nested Edge class -------------------------
class Edge:
    """Lightweight edge structure for a graph."""
    _slots_ = '_origin', '_destination', '_element'

    def _init_(self, u, v, x):
        """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._origin, self._destination)

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        return self._destination if v is self._origin else self._origin

    def element(self):
        """Return element associated with this edge."""
        return self._element

    def _hash_(self):  # will allow edge to be a map/set key
        return hash((self._origin, self._destination))