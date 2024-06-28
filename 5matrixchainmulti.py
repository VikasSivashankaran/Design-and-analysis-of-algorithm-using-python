import sys

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices in the chain
    m = [[0] * (n + 1) for _ in range(n + 1)]  # Table to store minimum costs
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Table to store optimal split positions
    
    for chain_length in range(2, n + 1):  # Chain length
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = sys.maxsize  # Initialize to infinity
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k  # Store optimal split position
    
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage:
matrix_dimensions = [40, 30, 20, 10]  # Example dimensions of matrices
min_cost_table, split_position_table = matrix_chain_order(matrix_dimensions)

print("Minimum cost of matrix chain multiplication:", min_cost_table[1][-1])
print("Optimal Parenthesization:", end=" ")
print_optimal_parens(split_position_table, 1, len(matrix_dimensions) - 1)
