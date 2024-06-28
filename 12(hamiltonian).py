import timeit
class HamiltonianCycle:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
    # Traditional method using adjacency matrix
    def is_safe(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:
            return False
        if v in path:
            return False
        return True
    def hamiltonian_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False
    def traditional_method(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonian_cycle_util(path, 1):
            print("No Hamiltonian cycle exists")
            return False
        self.print_solution(path)
        return True
    def print_solution(self, path):
        print("Hamiltonian cycle exists for Traditional: ")
        for i in range(self.V):
            print(f"({path[i]})", end=" ")
            if i < self.V - 1:
                print("-->", end=" ")
        print(f"({path[0]})")
class HamiltonianCycleBacktracking:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
    def is_safe(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:
            return False
        if v in path:
            return False
        return True
    def hamiltonian_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False
    def backtracking_method(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonian_cycle_util(path, 1):
            print("No Hamiltonian cycle exists")
            return False
        self.print_solution(path)
        return True
    def print_solution(self, path):
        print("Hamiltonian cycle exists for backtracking : ")
        for i in range(self.V):
            print(f"({path[i]})", end=" ")
            if i < self.V - 1:
                print("-->", end=" ")
        print(f"({path[0]})")
# Performance analysis
def performance_analysis(graph):
    print("Performance Analysis:")
    traditional_time = timeit.timeit(lambda: HamiltonianCycle(graph).traditional_method(), number=1)
    traditional_complexity = "O(n!)"  # Time complexity of the traditional method
    backtracking_time = timeit.timeit(lambda: HamiltonianCycleBacktracking(graph).backtracking_method(), number=1)
    backtracking_complexity = "O(2^n)"  # Time complexity of the backtracking method
    print("Time taken for traditional method: {:.10f} seconds, Time Complexity: {}".format(traditional_time, traditional_complexity))
    print("Time taken for backtracking method: {:.10f} seconds, Time Complexity: {}".format(backtracking_time, backtracking_complexity))
    if traditional_time < backtracking_time:
        print("Result: Traditional method is better to use.")
    elif backtracking_time < traditional_time:
        print("Result: Backtracking method is better to use.")
    else:
        print("Result: Both methods have similar performance.")
# Example graph
new_graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]
performance_analysis(new_graph)
