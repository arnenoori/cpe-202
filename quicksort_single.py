import random
import time

# Time Complexity: Time Complexity, O(N * log(N)), worst case O(n²)

# QUICKSORT 1 Way Implementation, typically faster

startTime = time.time()
def partition(alist, start, end):
    pivot = alist[start]
    low = start + 1
    high = end
    while True:
        while low <= high and alist[high] >= pivot:
            high = high - 1
        while low <= high and alist[low] <= pivot:
            low = low + 1
        if low <= high:
            alist[low], alist[high] = alist[high], alist[low]
        else:
            break
    alist[start], alist[high] = alist[high], alist[start]
    return high

def quick_sort(alist, start, end):
    if start >= end:
        return
    p = partition(alist, start, end)
    quick_sort(alist, start, p-1)
    quick_sort(alist, p+1, end)

# testing section
print("Time taken quicksort one way:",time.time() - startTime)
alist = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
quick_sort(alist, 0, len(alist) - 1)
print(alist)

# 3 WAY:

startTime1 = time.time()
def partition(arr, first, last, start, mid):
    pivot = arr[last]
    end = last

    while (mid[0] <= end):
        if (arr[mid[0]] < pivot):
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
        elif (arr[mid[0]] > pivot):
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
            end = end - 1
        else:
            mid[0] = mid[0] + 1

def quick_sort3(arr, first, last):
    if (first >= last):
        return
    if (last == first + 1):
        if (arr[first] > arr[last]):
            arr[first], arr[last] = arr[last], arr[first]
            return
    start = [first]
    mid = [first]
    partition(arr, first, last, start, mid)
    quick_sort3(arr, first, start[0] - 1)
    quick_sort3(arr, mid[0], last)
print("Time taken 3 way:",time.time() - startTime1)

# testing section

quicksortrun = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
quick_sort3(quicksortrun, 0, len(quicksortrun) - 1)
print(quicksortrun)

if __name__ == "__main__":
    array = [random.randint(0, 10000) for i in range(1000)]
    print(array)
    print(quick_sort(array))
    start = time.time
    quick_sort(array)
    print("Time taken")
    print(array)

'''
import random


class Quicksort():
    def __init__(alist):
        pivot = 0

    def swap(alist, x, y):
        alist[x], alist[y] = alist[y], alist[x]

    def partition(alist, left, right):
        pivot = alist[left]
        pivot_position = left
        for i in range(left + 1, right + 1):
            if alist[i] <= pivot:
                pivot_position += 1
                alist[i], alist[pivot_position] = alist[pivot_position], alist[i]
        alist[left], alist[pivot_position] = alist[pivot_position], alist[left]
        return pivot_position

    def partition_3way(alist, left, right):
        pivot, pivot_pos, num_equal = alist[left], left, 0
        for i in range(left + 1, right + 1):
            if alist[i] < pivot:
                pivot_pos += 1
                alist.swap(alist, i, pivot_pos)
            elif alist[i] == pivot:
                pivot_pos += 1
                num_equal += 1
                alist.swap(alist, i, pivot_pos)
        alist.swap(alist, left, pivot_pos)

        rearranged = 0
        while rearranged < num_equal:
            for j in reversed(range(left, pivot_pos - rearranged)):
                if alist[j] == pivot:
                    rearranged += 1
                    alist.swap(alist, j)
        return pivot_pos - num_equal, pivot_pos

    # ONE WAY Quick Sort

    # recursive implementation
    def quick_sort(alist, left, right):
        if left >= right:
            return alist

        # random number pivot
        random_pivot = random.randint(left, right)
        alist[left], alist[random_pivot] = alist[random_pivot], alist[left]

        pivot_position = alist.partition(alist, left, right)
        alist.quick_sort(alist, left, pivot_position - 1)
        alist.quick_sort(alist, pivot_position + 1, right)
        return alist

    # MEDIAN OF 3
    def quick_sort_3way(alist, left, right):
        while left < right:

            random_pivot = random.randint(left, right)
            alist[left], alist[random_pivot] = alist[random_pivot], alist[left]
            left_pivot_pos, right_pivot_pos = alist.partition_3way(alist, left, right)
            if (left_pivot_pos - left) < (right - right_pivot_pos):
                alist.quick_sort_3way(alist, left, left_pivot_pos - 1)
                left = right_pivot_pos + 1
            else:
                alist.quick_sort_3way(alist, right_pivot_pos + 1, right)
                right = left_pivot_pos - 1
        return alist

    def quick_sort1(alist):
        return alist.quick_sort_3way(alist, 0, len(alist) - 1)

'''