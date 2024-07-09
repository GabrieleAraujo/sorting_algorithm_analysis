import random
import tracemalloc
import timeit


# Font: https://github.com/AliDrgt/sorting-algorithms-comparison/blob/main/mergesort.py
def merge(arr, l, m, r):
    left_size = m - l + 1  # O(1)
    right_size = r - m     # O(1)

    left_array = arr[l:m + 1]   # O(n/2)
    right_array = arr[m + 1:r + 1]  # O(n/2)

    i = j = 0   # O(1)
    k = l       # O(1)

    while i < left_size and j < right_size:  # O(n)
        if left_array[i] <= right_array[j]:  # O(1)
            arr[k] = left_array[i]  # O(1)
            i += 1  # O(1)
        else:
            arr[k] = right_array[j]  # O(1)
            j += 1  # O(1)
        k += 1  # O(1)

    while i < left_size:  # O(n)
        arr[k] = left_array[i]  # O(1)
        i += 1  # O(1)
        k += 1  # O(1)

    while j < right_size:  # O(n)
        arr[k] = right_array[j]  # O(1)
        j += 1  # O(1)
        k += 1  # O(1)

def merge_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1  # O(1)
    if l < r:
        m = (l + r) // 2  # O(1)
        merge_sort(arr, l, m)   # T(n/2)
        merge_sort(arr, m + 1, r)  # T(n/2)
        merge(arr, l, m, r)  # O(n)
    return arr  # O(1)

def worst_case_merge(arr):
    if len(arr) <= 1:  # O(1)
        return arr
    if len(arr) == 2:  # O(1)
        return [arr[1], arr[0]]  # O(1)
    m = (len(arr) + 1) // 2  # O(1)
    left = worst_case_merge(arr[:m])  # T(n/2)
    right = worst_case_merge(arr[m:])  # T(n/2)
    return left + right  # O(n)

# Quick Sort with last element as pivot: https://github.com/diptangsu/Sorting-Algorithms/blob/master/Python/QuickSort.py
def quick_sort_last(arr, ini=0, fim=None):
    if fim is None:
        fim = len(arr)  # O(1)
    if fim - ini < 2:  # O(1)
        return arr
    pivot_index = partition_last(arr, ini, fim)  # O(n)
    quick_sort_last(arr, ini, pivot_index)  # T(n/2) 
    quick_sort_last(arr, pivot_index + 1, fim)  # T(n/2)
    return arr  # O(1)

def partition_last(arr, ini, fim):
    pivot = arr[fim - 1]  # O(1)
    i = ini  # O(1)
    for j in range(ini, fim - 1):  # O(n)
        if arr[j] <= pivot:  # O(1)
            arr[i], arr[j] = arr[j], arr[i]  # O(1)
            i += 1  # O(1)
    arr[i], arr[fim - 1] = arr[fim - 1], arr[i]  # O(1)
    return i  # O(1)

# Quick Sort with random pivot: https://github.com/dcorbin15/algos/blob/master/sorts/random_pivot_quick_sort.py
def quick_sort_random(arr, ini=0, fim=None):
    if fim is None:
        fim = len(arr)  # O(1)
    if fim - ini < 2:  # O(1)
        return arr
    pivot_index = partition_random(arr, ini, fim)  # O(n)
    quick_sort_random(arr, ini, pivot_index)  # T(n/2) em média
    quick_sort_random(arr, pivot_index + 1, fim)  # T(n/2) em média
    return arr  # O(1)

def partition_random(arr, ini, fim):
    pivot_index = random.randint(ini, fim - 1)  # O(1)
    arr[pivot_index], arr[fim - 1] = arr[fim - 1], arr[pivot_index]  # O(1)
    pivot = arr[fim - 1]  # O(1)
    i = ini  # O(1)
    for j in range(ini, fim - 1):  # O(n)
        if arr[j] <= pivot:  # O(1)
            arr[i], arr[j] = arr[j], arr[i]  # O(1)
            i += 1  # O(1)
    arr[i], arr[fim - 1] = arr[fim - 1], arr[i]  # O(1)
    return i  # O(1)

# Quick Sort with median of three pivot
def quick_sort_median(arr, ini=0, fim=None):
    if fim is None:
        fim = len(arr)  # O(1)
    if fim - ini < 2:  # O(1)
        return arr
    pivot_index = partition_median(arr, ini, fim)  # O(n)
    quick_sort_median(arr, ini, pivot_index)  # T(n/2) em média
    quick_sort_median(arr, pivot_index + 1, fim)  # T(n/2) em média
    return arr  # O(1)

def partition_median(arr, ini, fim):
    mid = (ini + fim - 1) // 2  # O(1)
    pivot_candidates = [(arr[ini], ini), (arr[mid], mid), (arr[fim - 1], fim - 1)]  # O(1)
    pivot_value, pivot_index = sorted(pivot_candidates)[1]  # O(1)
    arr[pivot_index], arr[fim - 1] = arr[fim - 1], arr[pivot_index]  # O(1)
    pivot = arr[fim - 1]  # O(1)
    i = ini  # O(1)
    for j in range(ini, fim - 1):  # O(n)
        if arr[j] <= pivot:  # O(1)
            arr[i], arr[j] = arr[j], arr[i]  # O(1)
            i += 1  # O(1)
    arr[i], arr[fim - 1] = arr[fim - 1], arr[i]  # O(1)
    return i  # O(1)

# Tim Sort (Python implementation)
def tim_sort(arr):
    arr.sort()
    return arr


# Time
def measure_performance(func, arr):
    tracemalloc.start()
    time_taken = timeit.timeit(lambda: func(arr.copy()), number=1)
    memory_usage = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    tracemalloc.reset_peak()
    return time_taken, memory_usage

# Best Case (ascending order)
def measure_best_case_performance(func, n):
    arr = list(range(n))
    return measure_performance(func, arr)

# Worst Case (descending order)
def measure_worst_case_performance(func, n):
    arr = list(range(n, 0, -1)) if func != merge_sort else worst_case_merge(list(range(n)))
    return measure_performance(func, arr)

# Average Case (Random, 5 steps)
def measure_average_case_performance(func, n):
    times = []
    memories = []
    for _ in range(5):
        arr = [random.randint(1, n) for _ in range(n)]
        time_taken, memory_used = measure_performance(func, arr)
        times.append(time_taken)
        memories.append(memory_used)
    avg_time = sum(times) / len(times)
    avg_memory = sum(memories) / len(memories)
    return avg_time, avg_memory
