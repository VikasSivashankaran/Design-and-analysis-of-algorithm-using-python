import networkx as nx
import matplotlib.pyplot as plt
import time

def multistage_shortest_path(graph, sources, destination):
    min_distances = {source: float('inf') for source in sources}
    shortest_paths = {}  
    
    for source in sources:
        if source in graph.nodes():  # Check if source node exists in the graph
            shortest_paths[source] = nx.single_source_dijkstra_path(graph, source)
            if destination in shortest_paths[source]:
                min_distances[source] = nx.single_source_dijkstra_path_length(graph, source)[destination]
        else:
            print(f"Warning: Source node '{source}' not found in the graph.")

    min_distance = min(min_distances.values())

    return min_distance, shortest_paths

def evaluate_performance():
    # Create a graph
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("a", "b", 3), ("a", "d", 4), ("a", "c", 5),
        ("b", "a", 3), ("b", "e", 6), ("b", "d", 1),
        ("c", "a", 5), ("c", "d", 2), ("c", "g", 4),
        ("d", "a", 4), ("d", "b", 1), ("d", "c", 2), ("d", "e", 1), ("d", "g", 3), ("d", "h", 5),
        ("e", "b", 6), ("e", "d", 1), ("e", "f", 2), ("e", "h", 6), ("e", "i", 4),
        ("f", "e", 2), ("f", "j", 5),
        ("g", "c", 4), ("g", "d", 3), ("g", "h", 3), ("g", "k", 6),
        ("h", "d", 5), ("h", "e", 6), ("h", "g", 3), ("h", "i", 6), ("h", "k", 8), ("h", "l", 7),
        ("i", "e", 4), ("i", "h", 6), ("i", "j", 3), ("i", "l", 5),
        ("j", "f", 5), ("j", "i", 3),
        ("k", "g", 6), ("k", "h", 7), ("k", "l", 8),
        ("l", "h", 7), ("l", "i", 5), ("l", "k", 8)
    ])
    
    sources = ['b']  # Adjust the source node here
    destination = 'l'

    start_time = time.perf_counter()
    min_distance, shortest_paths = multistage_shortest_path(G, sources, destination)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("Minimum distance from sources to destination:", min_distance)
    print("Execution time:", execution_time, "seconds")

    # Visualize the graph with highlighted shortest paths
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)  # positions for all nodes

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightgreen')

    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

    # Highlight nodes with different colors based on their shortest distances
    node_colors = []
    for node in G.nodes():
        if node in sources:
            node_colors.append('orange')  # Source node color
        elif node == destination:
            node_colors.append('red')  # Destination node color
        elif shortest_paths and node in shortest_paths:
            node_colors.append('yellow')  # Intermediate node color
        else:
            node_colors.append('lightgreen')
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

    # Draw shortest path
    shortest_path = shortest_paths[sources[0]][destination]
    edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2.5, edge_color='blue')

    plt.title("Graph with Shortest Paths")
    plt.axis('off')
    plt.show()

evaluate_performance()
