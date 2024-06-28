#by using quick and bubble sort in a single program ,call these sorting method for every iteration of datasets for 3 set of data call both sort and also produce timing in seconds and find difference betwween time and print it as a table for 3 set of data .Number of data as random data by using random method in python
import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    return sorted_data, elapsed_time

# Get data size from user input
data_size = int(input("Enter the data size: "))

# Generate random data
data = generate_random_data(data_size)

# Measure time for Quick Sort
_, quick_sort_time = measure_time(quick_sort, data)
print(f"Quick Sort Time for {data_size} data points: {quick_sort_time:.6f} seconds")

# Measure time for Bubble Sort
_, bubble_sort_time = measure_time(bubble_sort, data)
print(f"Bubble Sort Time for {data_size} data points: {bubble_sort_time:.6f} seconds")

# Print time difference
time_difference = bubble_sort_time - quick_sort_time
print(f"Time Difference: {time_difference:.6f} seconds")
