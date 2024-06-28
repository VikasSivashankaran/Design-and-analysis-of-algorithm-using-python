class MultistageGraph:
    def __init__(self, num_stages):
        self.num_stages = num_stages
        self.graph = [[] for _ in range(num_stages)]
        self.num_vertices = 0
    
    def add_edge(self, stage, u, v, weight):
        self.graph[stage].append((u, v, weight))
        self.num_vertices = max(self.num_vertices, u, v)
    
    def shortest_path(self, source):
        # Initialize distance and predecessor arrays
        dist = [float('inf')] * (self.num_vertices + 1)
        dist[source] = 0
        pred = [None] * (self.num_vertices + 1)

        # Traverse the graph forwards
        for stage in range(self.num_stages):
            for u, v, weight in self.graph[stage]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    pred[v] = u
        
        # Traverse the graph backwards to update distances
        for stage in range(self.num_stages - 2, -1, -1):
            for u, v, weight in self.graph[stage]:
                if dist[v] + weight < dist[u]:
                    dist[u] = dist[v] + weight
                    pred[u] = v
        
        return dist, pred

    def print_shortest_path(self, source, target):
        dist, pred = self.shortest_path(source)
        
        # If target is unreachable, print appropriate message
        if dist[target] == float('inf'):
            print(f"No path from node {source} to node {target}")
            return
        
        # Reconstruct the shortest path
        path = [target]
        current_node = target
        while pred[current_node] is not None:
            path.insert(0, pred[current_node])
            current_node = pred[current_node]
        
        print(f"Shortest path from node {source} to node {target}: {' -> '.join(map(str, path))}, distance: {dist[target]}")

# Sample usage:
g = MultistageGraph(4)

g.add_edge(0, 0, 1, 2)
g.add_edge(0, 0, 2, 1)
g.add_edge(1, 1, 3, 5)
g.add_edge(1, 2, 3, 4)
g.add_edge(2, 3, 4, 2)
g.add_edge(2, 3, 5, 6)
g.add_edge(3, 4, 6, 1)

source_vertex = 0
target_vertex = 6

g.print_shortest_path(source_vertex, target_vertex)
