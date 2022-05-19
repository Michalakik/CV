import timeit

def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

def partition(arr, low, high):
    med = median_of_three(low, high // 2, high)
    arr[med], arr[high] = arr[high], arr[med]
    i = low

    for j in range(low, high):

        if arr[j] <= arr[high]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort_median(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quick_sort_median(arr, low, pi - 1)
        quick_sort_median(arr, pi + 1, high)

def check_time(arr):
    start = timeit.default_timer()
    quick_sort_median(arr, 0, len(arr) - 1)  # wywolanie
    end = timeit.default_timer()
    time = end - start
    return time
