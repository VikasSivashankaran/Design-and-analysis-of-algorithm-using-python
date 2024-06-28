def subset_sum_dp(nums, target):
    n = len(nums)

    # Initialize a boolean table dp
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # An empty subset always sums up to zero
    for i in range(n + 1):
        dp[i][0] = True

    # Update the dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                
            else:
                dp[i][j] = dp[i - 1][j]

    # Check if there exists a subset with the given sum
    if not dp[n][target]:
        print(f"No subset is found ")
        return

    # Traceback to find and print all subsets
    
    print_all_subsets(nums, n, target, dp)

def print_all_subsets(nums, i, target, dp, current_subset=[]):
    
    if i == 0 and target == 0:
        
        print(f"Subset found from {S} : {current_subset[::-1]}")
        return

    if i == 0 or target < 0:
        return

    # If current element is not included in the subset
    if dp[i - 1][target]:
        print_all_subsets(nums, i - 1, target, dp, current_subset)

    # If current element is included in the subset
    if target >= nums[i - 1] and dp[i - 1][target - nums[i - 1]]:
        print_all_subsets(nums, i - 1, target - nums[i - 1], dp, current_subset + [nums[i - 1]])

# Example usage
S = [1, 2, 5, 6, 8]
d = 9
subset_sum_dp(S, d)

# Compare with other values
other_values = [10]
for val in other_values:
    print(f"\nChecking for subset with sum {val}:")
    subset_sum_dp(S, val)





'''he Subset Sum Problem is a classic computational problem where we aim to find a subset of a given set of positive integers such that their sum equals a specified positive integer. Let’s delve into the details and explore different approaches to solve this problem.

Problem Statement
Given a set of non-negative integers S = {s1, s2, …, sn} and a target sum d, we want to determine whether there exists a non-empty subset of S whose sum equals d.

Examples
For instance, consider the set S = {1, 2, 5, 6, 8} and d = 9. In this case, there are two valid solutions:
Subset 1: {1, 2, 6}
Subset 2: {1, 8}
However, if we take S = {3, 34, 4, 12, 5, 2} and d = 30, there is no subset that adds up to 30.
Approaches to Solve Subset Sum



Dynamic Programming Approach:
    
Initialization: The function initializes a boolean table dp with dimensions (n+1) x (target+1), where n is the length of the input array nums. The table is initialized with False values. Additionally, the subsets with a sum of 0 are marked as True (an empty subset).

Updating the dp table: The nested loops iterate over each element of nums and each possible target sum. For each element, it checks if including or excluding the current element can achieve the target sum. The logic is based on the recurrence relation for the subset sum problem.

Check for the existence of a subset: After updating the dp table, the function checks if there exists a subset with the given sum (target). If not, it prints a message and returns.

Traceback and Printing Subsets: If a subset is found, the function calls print_all_subsets to trace back and print all the subsets contributing to the target sum.

print_all_subsets function: This function is responsible for recursively printing all subsets that contribute to the target sum. It starts from the bottom-right corner of the dp table and explores different possibilities.

Example usage: The function is then called with an example set S = [1, 2, 5, 6, 8] and target sum d = 9..'''