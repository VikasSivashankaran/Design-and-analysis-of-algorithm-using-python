import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def evaluate_performance(graph, start):
    start_time = time.perf_counter()
    distances = dijkstra(graph, start)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

graph = {
    0: [(1, 1), (2, 2), (3, 5)],
    1: [(4, 4), (5, 11)],
    2: [(4, 9), (5, 5), (6, 16)],
    3: [(6, 2)],
    4: [(7, 18)],
    5: [(7, 13)],
    6: [(7, 2)],
    7: []
}

start_node = 0

distances = dijkstra(graph, start_node)

G = nx.DiGraph()

for node, neighbors in graph.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=18, font_weight='bold', arrows=False)

node_colors = []
for node in G.nodes():
    if node == start_node:
        node_colors.append('orange')  
    elif distances[node] == float('inf'):
        node_colors.append('yellow')  
    else:
        node_colors.append('lightgreen')  

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)

edge_labels = {(n1, n2): d['weight'] for n1, n2, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Shortest Path Graph')
plt.show()

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print("To node", str(node) + ":", distance)

execution_time = evaluate_performance(graph, start_node)
print("Performance evaluation of Dijkstra's algorithm:", "{:.10f}".format(execution_time), "seconds")
