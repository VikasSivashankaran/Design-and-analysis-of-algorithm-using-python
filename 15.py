import heapq
def tsp_branch_and_bound(graph):
    n = len(graph)
    INF = float('inf')
    # Helper function to calculate the lower bound of a given path
    def calculate_lower_bound(path):
        lb = 0
        n = len(path)
        for i in range(n):
            if i < n - 1:
                lb += graph[path[i]][path[i + 1]]
            else:
                lb += graph[path[i]][path[0]]  # Add the cost to return to the starting node
        return lb
    # Initialize variables
    min_cost = INF
    min_path = []
    # Initialize priority queue (min heap) to explore the search space
    pq = [(calculate_lower_bound([i]), [i]) for i in range(n)]
    heapq.heapify(pq)
    # Branch and Bound Algorithm
    while pq:
        lower_bound, path = heapq.heappop(pq)
        # If the lower bound is greater than the current minimum cost, prune this branch
        if lower_bound >= min_cost:
            continue
        # If the path includes all nodes and the cost is less than current minimum cost, update min_cost and min_path
        if len(path) == n and lower_bound < min_cost:
            min_cost = lower_bound
            min_path = path
            continue
        # Expand the current node by adding adjacent nodes to the path
        for i in range(n):
            if i not in path:
                new_path = path + [i]
                new_lower_bound = calculate_lower_bound(new_path)
                # Prune branches where the lower bound exceeds the current minimum cost
                if new_lower_bound < min_cost:
                    heapq.heappush(pq, (new_lower_bound, new_path))
    return min_cost, min_path
# Example usage
graph = [
    [0, 3, 1, 6],
    [3, 0, 7, 5],
    [1, 7, 0, 4],
    [6, 5, 4, 0]
]
min_cost, min_path = tsp_branch_and_bound(graph)
print("Minimum cost:", min_cost)
print("Minimum path:", min_path)
