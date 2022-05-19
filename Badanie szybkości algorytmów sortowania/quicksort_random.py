import timeit
import random
import sys

def quicksort_random(arr, low, high):
    if (low < high):

        pivotindex = partitionrand(arr, low, high)

        quicksort_random(arr, low, pivotindex)
        quicksort_random(arr, pivotindex + 1, high)

def partitionrand(arr, low, high):
    randpivot = random.randrange(low, high)

    arr[low], arr[randpivot] = \
        arr[randpivot], arr[low]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = low  # pivot
    i = low - 1
    j = high + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def check_time_random(arr):
    start = timeit.default_timer()
    quicksort_random(arr, 0, len(arr) - 1)  # wywolanie
    end = timeit.default_timer()
    time = end - start
    return time
