class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost


def bound(i, current_weight, current_value, items, capacity):
    total_weight = current_weight
    total_value = current_value

    while i < len(items) and total_weight + items[i].weight <= capacity:
        total_weight += items[i].weight
        total_value += items[i].value
        i += 1

    if i < len(items):
        total_value += (capacity - total_weight) * items[i].cost

    return total_value

def knapsack_branch_and_bound(weights, values, capacity):
    items = [Item(weights[i], values[i], i) for i in range(len(weights))]
    items.sort(reverse=True)

    max_value = 0
    max_taken = [0] * len(weights)

    stack = [(0, 0, 0, [0] * len(weights))]

    while stack:
        i, current_weight, current_value, taken = stack.pop()

        if current_weight > capacity:
            continue

        if i == len(items) or bound(i, current_weight, current_value, items, capacity) <= max_value:
            if current_value > max_value:
                max_value = current_value
                max_taken = taken[:]
            continue

        stack.append((i + 1, current_weight, current_value, taken))

        taken_copy = taken[:]
        taken_copy[items[i].index] = 1
        stack.append((i + 1, current_weight + items[i].weight,
                      current_value + items[i].value, taken_copy))

    return max_value, max_taken

# New example usage
weights = [15, 25, 35, 45]
values = [80, 120, 160, 200]
capacity = 60

# Call the function with the new values
max_value, max_taken = knapsack_branch_and_bound(weights, values, capacity)
print("Maximum value:", max_value)
print("Items taken:", max_taken)