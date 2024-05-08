import timeit
import random

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    
    merged.extend(right[right_index:])
    
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    return sorted(arr)

arr = [random.randint(0, 1000) for _ in range(1000)]

# Вимірюємо час сортування злиттям
merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=100)
print("Час сортування злиттям:", merge_sort_time)

# Вимірюємо час сортування вставками
insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=100)
print("Час сортування вставками:", insertion_sort_time)

# Вимірюємо час сортування Timsort
timsort_time = timeit.timeit(lambda: timsort(arr.copy()), number=100)
print("Час сортування Timsort:", timsort_time)
