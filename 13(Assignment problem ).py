import heapq
import copy
import time
N = 4
# State space tree node
class Node:
    def __init__(self, x, y, assigned, parent):
        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.workerID = x
        self.jobID = y
        self.assigned = copy.deepcopy(assigned)
        if y != -1:
            self.assigned[y] = True
    # Define less-than comparison for Node instances
    def __lt__(self, other):
        return self.cost < other.cost
# Custom heap class with push and pop functions
class CustomHeap:
    def __init__(self):
        self.heap = []
    def push(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
def new_node(x, y, assigned, parent):
    return Node(x, y, assigned, parent)
def calculate_cost(projects_skills, developers_skills, x, y):
    cost = 0
    for i in range(len(projects_skills[y])):
        cost += abs(projects_skills[y][i] - developers_skills[x][i])
    return cost
def print_assignments(min_node, projects_skills):
    if min_node.parent is None:
        return
    print_assignments(min_node.parent, projects_skills)
    print("Assign Project {} to Developer {}".format(min_node.jobID + 1, min_node.workerID + 1))
# Finds minimum skill gap using Branch and Bound
def find_min_cost(projects_skills, developers_skills):
    pq = CustomHeap()
    # initialize heap to dummy node with cost 0
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.workerID = -1
    # Add dummy node to list of live nodes;
    pq.push(root)
    while True:
        min_node = pq.pop()
        i = min_node.workerID + 1
        if i == N:
            print_assignments(min_node, projects_skills)
            return min_node.cost
        for j in range(N):
            if not min_node.assigned[j]:
                child = new_node(i, j, min_node.assigned, min_node)
                child.pathCost = min_node.pathCost + calculate_cost(projects_skills, developers_skills, i, j)
                child.cost = child.pathCost
                pq.push(child)
if __name__ == "__main__":
    # Skills required for each project
    projects_skills = [
        [3, 2, 4, 5],
        [1, 2, 1, 4],
        [2, 3, 2, 3],
        [4, 1, 3, 2]
    ]
    # Skills of each developer
    developers_skills = [
        [5, 4, 3, 2],
        [3, 2, 5, 4],
        [4, 5, 2, 3],
        [2, 3, 4, 5]
    ]
    optimal_cost = find_min_cost(projects_skills, developers_skills)
    if optimal_cost is not None:
        print("\nOptimal Skill Gap is {}".format(optimal_cost))
    else:
        print("\nNo optimal solution found.")
