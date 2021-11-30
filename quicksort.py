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


