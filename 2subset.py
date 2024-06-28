#recursive approach

def subset_sum(nums, target, current_subset, result):
    if target == 0:
        result.append(current_subset.copy())
        return

    if not nums or target < 0:
        return

    # Include the current element in the subset
    current_subset.append(nums[0])
    subset_sum(nums[1:], target - nums[0], current_subset, result)
    current_subset.pop()

    # Exclude the current element from the subset
    subset_sum(nums[1:], target, current_subset, result)

def find_subset_sum(nums, target):
    result = []
    subset_sum(nums, target, [], result)

    if not result:
        print("No subset found.")
    else:
        print("Subset(s) found:", result)

# Example usage 1
S1 = [1, 2, 5, 6, 8]
d1 = 9
find_subset_sum(S1, d1)

# Example usage 2
S2 = [3, 4, 7, 9]
d2 = 12
find_subset_sum(S2, d2)

# Additional comparisons and messages
if d1 < 0 or d2 < 0:
    print("Invalid target value. Target should be a non-negative integer.")
elif not S1 and not S2:
    print("Both input lists are empty. Please provide at least one non-empty list.")
elif not S1:
    print("The first input list is empty. Please provide a non-empty list.")
elif not S2:
    print("The second input list is empty. Please provide a non-empty list.")
else:
    print("Comparison with other examples:")
    print("Example 1 - Target value:", d1, "Input list:", S1)
    print("Example 2 - Target value:", d2, "Input list:", S2)




'''he Subset Sum Problem is a classic computational problem where we aim to find a subset of a given set of positive integers such that their sum equals a specified positive integer. Let’s delve into the details and explore different approaches to solve this problem.

Problem Statement
Given a set of non-negative integers S = {s1, s2, …, sn} and a target sum d, we want to determine whether there exists a non-empty subset of S whose sum equals d.

Examples
For instance, consider the set S = {1, 2, 5, 6, 8} and d = 9. In this case, there are two valid solutions:
Subset 1: {1, 2, 6}
Subset 2: {1, 8}
However, if we take S = {3, 34, 4, 12, 5, 2} and d = 30, there is no subset that adds up to 30.
Approaches to Solve Subset Sum

Recursive Approach:
    
We can recursively explore two possibilities for each element in the set:
Include the current element in the subset (subtract its value from the target sum).
Exclude the current element from the subset (keep the target sum unchanged).
The base cases are:
If the target sum becomes zero, we have found a valid subset.
If we exhaust all elements in the set, but the target sum is still non-zero, no valid subset exists.
The time complexity of this approach is exponential (O(2^n)).'''