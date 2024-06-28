def subset_sum_backtracking(a, target_sum):
    result = []

    def backtrack(index, current_sum, subset):
        if current_sum == target_sum:
            result.append(subset[:]) 
            return
        if index >= len(a) or current_sum > target_sum:
            return

        # Include current element
        subset.append(a[index])
        backtrack(index + 1, current_sum + a[index], subset)
        subset.pop()  # Backtrack

        backtrack(index + 1, current_sum, subset)

    backtrack(0, 0, [])
    return result

a = list(map(int, input("Enter the list of numbers separated by space: ").split()))
target_sum = int(input("Enter the target sum: "))

result = subset_sum_backtracking(a, target_sum)
if result:
    print("Subsets that sum up to", target_sum, ":", result)
else:
    print("No subsets found that sum up to", target_sum)