import random

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        
    def dfs_random_team(self, start_node, team_size):
        visited = set()
        team = []
        
        def dfs(node):
            if len(team) >= team_size:
                return
            visited.add(node)
            team.append(node)
            random.shuffle(self.graph[node])
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start_node)
        return team

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('Start', 'Sami')
    g.add_edge('Simanga', 'Gontse')
    g.add_edge('Sami', 'Taiwo')
    g.add_edge('Sami', 'Simanga')
    g.add_edge('Gontse', 'Taiwo')
    g.add_edge('Gontse', 'Sami')
    g.add_edge('Taiwo', 'Simanga')
    
    
    team_size = 3
    start_node = 'Start'
    team = g.dfs_random_team(start_node, team_size)
    print("Selected team:", team)
