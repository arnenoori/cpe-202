import random
import time


startTime = time.time()
# typically faster, esp with larger count
# Time Complexity: O(n)
def insertion_sort(alist):
    swapsmade = 0
    checksmade = 0
    for fill in range(len(alist)):
        value = alist[fill]
        valueindex = fill
        checksmade += 1
        # moving the value
        while valueindex > 0 and value < alist[valueindex - 1]:
            alist[valueindex] = alist[valueindex - 1]
            valueindex -= 1
            checksmade += 1
            swapsmade += 1
        alist[valueindex] = value
    print(alist)
    swapsnchecks = "{} swaps were made. {} checks were made.".format(swapsmade, checksmade)
    return swapsnchecks

print("Time taken insertion:",time.time() - startTime)
print(insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(insertion_sort([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Now beginning selection sort:")

startTime1 = time.time()
# not as fast, but faster in some cases with smaller count
# Time Complexity: O(n²)
def selection_sort(alist):
    swapsmade = 0
    checksmade = 0
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       checksmade += 1
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       checksmade += 1
       swapsmade += 1
    swapsnchecks = "{} swaps were made. {} checks were made.".format(swapsmade, checksmade)
    return swapsnchecks

print("Time taken selection:",time.time() - startTime1)
L = [54,26,93,17,77,31,44,55,20]
print(L)
selection_sort(L)
print(L)
print(selection_sort(L))

if __name__ == "__main__":
    array = [random.randint(0, 10000) for i in range(1000)]
    print(array)
    print(selection_sort(array))
    selection_sort(array)
    print(array)

'''
L = random.sample(range(0, 1000), 100)
Sorting.insertion_sort([10, 17, 40])
t1 = time()
Sorting.insertion_sort([L])
t2 = time()
print("selection sort time: %8.4f" % (t2-t1))

import time
import random

# time library import with start and end time

def insertion_sort(alist):
    count = 0
    for i in range(1, len(alist)):
        j = i
        while j > 0 and alist[j] < alist[j - 1]:
            alist[j], alist[j - 1] = alist[j - 1], alist[j]
            j -= 1
            count += 1
    return alist, count

def selection_sort(alist):
    n = len(alist)
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
        count += 1
    return alist, count

def test(self):
    x = random.sample(range(0, 1000), 100)
    start = time.time()
    self.insertion_sort(x)
    elapsed = (time.time() - start)
    print("Time taken for Insertion = ", elapsed)


from random import shuffle


def insertion_sort(alist):
    count = 0
    start_time = time.time()
    alist = random.sample(range(0, 1000), 100)
    indexing_length = range(1, len(alist))
    for i in indexing_length:
        value_to_sort = alist[i]
        while alist[i - 0] > value_to_sort and i > 0:
            alist[i], alist[i - 1] = alist[i - 1], alist[i]
            i -= 1
            count += 1
    print(time.time() - start_time, "seconds")
    return alist

    def test(self):
        alist = list
        list = r.sample(range(0, 1000), 100)
        print(alist)

sort = Sorting()
testlist = r.sample(range(0, 1000), 100)
sort.insertion_sort.alist


def generate_numbers(alist, number_elements=1000, max_integer=100):
    from random import randint
    for _ in range(number_elements):
        alist = randint(0, max_integer)
    return alist


alist = Sorting()
alist = generate_numbers(alist)

HOW TO DO THE RANDOM THING:
list = []
for(i in range(1000)): ... range greater than number of elements
then call..
    alist.append(randint())

for i in range(1000):
    Sorting.insertion_sort([i])
    Sorting.insertion_sort.append(random.randint([i]))

insertion_sort.alist = []
insertion_sort.alist = [r.randint(0, 100) for i in range(0, 1000)].insertion_sort.alist()
print(insertion_sort.alist)

import random
import time

# insertion sort (x)


def insertion(alist):
    count = 0
    for index in range(1, len(alist)):
        value = alist[index]
        i = index - 1
        while i >= 0 and (value < alist[i]):
            alist[i + 1] = alist[i]  # shift number in slot i right to slot i+1
            alist[i] = value  # shift value left into slot i
            i = i - 1
            count += 1
    return alist, count


# insertion sort (y)

def selection(alist):
    n = len(alist)
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
        count += 1
    return alist, count


# bubble sort (z)

def bubble(list):
    count = 0
    length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
            count += 1
    return list, count



x = random.sample(range(0, 1000), 100)

selection(x)
insertion(x)
bubble(x)



import random
import time
import matplotlib.pyplot as plt

def insertion(list):
    for index in range(1 ,len(list)):
        value = list[index]
        i = index - 1
        while i>= 0 and (value < list[i]):
            list[i + 1] = list[i]
            list[i] = value
            i = i - 1


def mean(a):
    return sum(a) / len(a)


def test():
    graph_list_x = []

    find_all_list_y = []
    find_all_sorted_list_y = []
    find_all_worst_list_y = []

    random_lists = []
    sorted_list_y = []
    worst_list_y = []
    range_num = 1000

    # creating 15 random lists
    for one_list in range(15):
        random_lists.append([])
        for x in range(range_num):
            random_lists[one_list].append(random.randint(1, 1001))
        range_num += 1000
        graph_list_x.append(len(random_lists[one_list]))

        print(random_lists[one_list])

    # creating 15 random best sorted lists
    for one_item in range(15):
        sorted_list_y.append(sorted(random_lists[one_item]))

    # creating 15 random worst sorted lists
    for one_item in range(15):
        worst_list_y.append(sorted(random_lists[one_item], reverse=True))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (average case)
    for i in range(50):
        graph_list_y = []
        for one_item in range(15):
            pass_list = random_lists[one_item][:]
            start = time.time()
            insertion(pass_list)
            elapsed = (time.time() - start)
            print(pass_list)

            graph_list_y.append(elapsed)

        find_all_list_y.append(graph_list_y)

    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (best case)
    for i in range(50):
        graph_sorted_list_y = []
        for one_item in range(15):
            pass_list = sorted_list_y[one_item][:]
            start = time.time()
            insertion(pass_list)
            elapsed = (time.time() - start)
            print(pass_list)

            graph_sorted_list_y.append(elapsed)

        find_all_sorted_list_y.append(graph_sorted_list_y)

    final_sorted_avg_list_y = list(map(mean, zip(*find_all_sorted_list_y)))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (worst case)
    for i in range(50):
        graph_worst_list_y = []
        for one_item in range(15):
            pass_list = worst_list_y[one_item][:]
            start = time.time()
            insertion(pass_list)
            elapsed = (time.time() - start)
            print(pass_list)

            graph_worst_list_y.append(elapsed)

        find_all_worst_list_y.append(graph_worst_list_y)

    final_worst_avg_list_y = list(map(mean, zip(*find_all_worst_list_y)))

    # plotting the graph
    plt.xlabel('List Length')
    plt.ylabel('Time Taken')
    plt.plot(graph_list_x, final_avg_list_y, label='Average Case')
    plt.plot(graph_list_x, final_sorted_avg_list_y, label='Best Case')
    plt.plot(graph_list_x, final_worst_avg_list_y, label='Worst Case')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    test()

import random

#insertion sort (x)

def insertion(list):
    count = 0
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i + 1] = list[i]  # shift number in slot i right to slot i+1
            list[i] = value  # shift value left into slot i
            i = i - 1
            count += 1
    return count


# insertion sort (y)

def selection(alist):
    n = len(alist)
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
        count += 1
    return count


# bubble sort (z)

def bubble(list):
    count = 0
    length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
            count += 1
    return count


def test_1000():
    import time
    print("Test of 1000 random numbers")
    x = random.sample(range(0, 10000), 1000)
    y = random.sample(range(0, 10000), 1000)


    # SELECTION SORT

    start = time.time()
    selection(x)
    end = time.time()
    print("Time taken for selection = " + str(1000 * (end - start)) + " milliseconds")

    # INSERTION SORT

    start = time.time()
    insertion.insertion(y)
    end = time.time()
    print("Time taken for insertion = " + str(1000 * (end - start)) + " milliseconds")

    # BUBBLE SORT



if __name__ == '__main__':
    import time

'''
