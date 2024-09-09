import time
import random
import numpy as np

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Performance Comparison
def performance_comparison():
    sizes = [100, 1000, 5000, 10000]
    data_types = ['sorted', 'reverse_sorted', 'random']
    results = {}

    for size in sizes:
        results[size] = {}
        for dtype in data_types:
            data = []
            if dtype == 'sorted':
                data = list(range(size))
            elif dtype == 'reverse_sorted':
                data = list(range(size, 0, -1))
            elif dtype == 'random':
                data = [random.randint(0, size) for _ in range(size)]

            # Measure Quick Sort
            start_time = time.time()
            quick_sort(data.copy())
            quick_sort_time = time.time() - start_time

            # Measure Merge Sort
            start_time = time.time()
            merge_sort(data.copy())
            merge_sort_time = time.time() - start_time

            results[size][dtype] = {
                'Quick Sort': quick_sort_time,
                'Merge Sort': merge_sort_time
            }

    return results

# Run the performance comparison
comparison_results = performance_comparison()

# Print the results
for size, data_results in comparison_results.items():
    print(f"Array Size: {size}")
    for dtype, times in data_results.items():
        print(f"  Data Type: {dtype}")
        print(f"    Quick Sort Time: {times['Quick Sort']} seconds")
        print(f"    Merge Sort Time: {times['Merge Sort']} seconds")
    print()
