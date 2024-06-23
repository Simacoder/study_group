class Graph:
    def __init__(self):
        self.adj_map = {}

    def add_vertex(self, v):
        if v not in self.adj_map:
            self.adj_map[v] = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_map:
            self.add_vertex(u)
        if v not in self.adj_map:
            self.add_vertex(v)
        self.adj_map[u][v] = weight
        self.adj_map[v][u] = weight  # If undirected, add the reverse edge as well

    def remove_vertex(self, v):
        if v not in self.adj_map:
            return
        
        # Remove all edges pointing to v
        for neighbor in list(self.adj_map[v].keys()):
            del self.adj_map[neighbor][v]
        
        # Remove vertex v itself
        del self.adj_map[v]

    def __str__(self):
        return str(self.adj_map)


# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("Graph before removing vertex 'D':")
print(g)

g.remove_vertex('D')

print("\nGraph after removing vertex 'D':")
print(g)



"""
Explanation:
Graph Initialization:

__init__(self): Initializes the graph with an empty adjacency map.
Adding Vertices and Edges:

add_vertex(self, v): Adds a vertex 
v
v to the adjacency map.
add_edge(self, u, v, weight=1): Adds an edge between vertices 
u
u and 
v
v. This implementation assumes an undirected graph by adding the reverse edge as well.
Removing a Vertex:

remove_vertex(self, v): Removes the vertex 
v
v and all edges associated with it.
Step 1: Check if the vertex 
v
v exists in the adjacency map. If not, return immediately.
Step 2: Iterate over all neighbors of 
v
v (i.e., all vertices that have an edge to 
v
v) and delete the edge from each neighbor to 
v
v. This ensures we remove all edges pointing to 
v
v.
Step 3: Delete the vertex 
v
v from the adjacency map.
Example Usage:

The example creates a graph, adds edges, prints the graph, removes a vertex, and prints the graph again to show the result.

"""
