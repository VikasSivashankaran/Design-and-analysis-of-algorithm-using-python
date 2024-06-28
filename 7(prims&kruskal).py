import networkx as nx
import matplotlib.pyplot as plt
import timeit

def prims_algorithm(graph):
    start_time = timeit.default_timer()
    mst = nx.minimum_spanning_tree(graph)
    end_time = timeit.default_timer()
    return mst, end_time - start_time

def kruskals_algorithm(graph):
    start_time = timeit.default_timer()
    mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')
    end_time = timeit.default_timer()
    return mst, end_time - start_time

def draw_graph(graph, title):
    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, labels={node: chr(65 + node) for node in graph.nodes()}, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

def display_mst(mst, original_graph):
    total_weight = sum(weight for (_, _, weight) in mst.edges(data='weight'))
    for u, v, weight in mst.edges(data='weight'):
        node_u = list(original_graph.nodes())[u]
        node_v = list(original_graph.nodes())[v]
        print(f"Edge: {chr(65 + node_u)} - {chr(65 + node_v)}, Weight: {weight}")
    print(f"Total Weight of MST: {total_weight}")

def main():
    # Define the graph
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 3), (2, 3, 5),(3,0,2)])

    # Display the original graph
    draw_graph(G, "Original Graph")

    # Perform Prim's algorithm
    prims_tree, prims_time = prims_algorithm(G.copy())  # Create a copy of the graph to avoid modifying the original
    print("\nPrim's Minimum Spanning Tree:")
    display_mst(prims_tree, G)

    # Perform Kruskal's algorithm
    kruskals_tree, kruskals_time = kruskals_algorithm(G.copy())  # Create a copy of the graph to avoid modifying the original
    print("\nKruskal's Minimum Spanning Tree:")
    display_mst(kruskals_tree, G)

    # Performance Evaluation
    print("\nPrim's Algorithm Time: {:.10f}".format(prims_time))
    print("Kruskal's Algorithm Time: {:.10f}".format(kruskals_time))

if __name__ == "__main__":
    main()
