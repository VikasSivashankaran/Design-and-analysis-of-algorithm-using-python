class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, state, row, col):
        # Check if a queen can be placed on board[row][col]
        # Returns False if the queen conflicts with another queen on the board
        for i in range(row):
            if state[i] == col or abs(i - row) == abs(state[i] - col):
                return False
        return True

    def solve_n_queens(self):
        # Initialize the stack with an empty state
        stack = [[]]

        while stack:
            # Pop a state from the stack
            state = stack.pop()

            # If the state is a complete solution, add it to the solutions list
            if len(state) == self.n:
                self.solutions.append(state)
                continue

            # Generate legal moves from the current state
            row = len(state)
            for col in range(self.n):
                if self.is_safe(state, row, col):
                    new_state = state + [col]
                    stack.append(new_state)

        return self.solutions

    def print_solution_table(self, solution):
        board = [['*' for _ in range(self.n)] for _ in range(self.n)]
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        
        for row in board:
            print(' '.join(row))

# Example usage
solver = NQueensSolver(4)
solutions = solver.solve_n_queens()
print("Number of solutions found:", len(solutions))
for idx, solution in enumerate(solutions, start=1):
    print(f"Solution {idx}:")
    solver.print_solution_table(solution)
    print()
