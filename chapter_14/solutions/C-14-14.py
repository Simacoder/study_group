class Graph:
    def __init__(self, directed=False):
        self.adj_map = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_map:
            self.adj_map[v] = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_map:
            self.add_vertex(u)
        if v not in self.adj_map:
            self.add_vertex(v)
        self.adj_map[u][v] = weight
        if not self.directed:
            self.adj_map[v][u] = weight

    def remove_edge(self, u, v):
        if u in self.adj_map and v in self.adj_map[u]:
            del self.adj_map[u][v]
        if not self.directed and v in self.adj_map and u in self.adj_map[v]:
            del self.adj_map[v][u]

    def __str__(self):
        return str(self.adj_map)


# Example usage
g = Graph(directed=False)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("Graph before removing edge ('A', 'C'):")
print(g)

g.remove_edge('A', 'C')

print("\nGraph after removing edge ('A', 'C'):")
print(g)


"""
Explanation:
Graph Initialization:

__init__(self, directed=False): Initializes the graph with an empty adjacency map and a flag indicating whether the graph is directed or undirected. By default, the graph is undirected.
Adding Vertices and Edges:

add_vertex(self, v): Adds a vertex 
v
v to the adjacency map.
add_edge(self, u, v, weight=1): Adds an edge between vertices 
u
u and 
v
v with an optional weight. If the graph is undirected, it also adds the reverse edge.
Removing an Edge:

remove_edge(self, u, v): Removes the edge from 
u
u to 
v
v.
Step 1: Check if 
u
u and 
v
v are in the adjacency map and if there is an edge from 
u
u to 
v. If so, delete the edge.
Step 2: If the graph is undirected, also check if v
v and 
u
u are in the adjacency map and if there is an edge from v
v to u
u. If so, delete the reverse edge.
Example Usage:

The example creates a graph, adds edges, prints the graph, removes an edge, and prints the graph again to show the result.
This implementation ensures that the remove_edge method runs in 
O(1)
O(1) time. This is achieved by performing constant-time dictionary operations to delete the edges.

"""
