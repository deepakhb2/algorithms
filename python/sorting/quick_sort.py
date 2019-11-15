# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
# There are many different versions of quickSort that pick pivot in different ways.
# 1. Always pick first element as pivot.
# 2. Always pick last element as pivot (implemented below)
# 3. Pick a random element as pivot.
# 4. Pick median as pivot.


# [0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99]
# 
# pivotal_value = 99
# partition_index = 1
# i = 1
# array[1] < 99
# swap(array, 1, 1)
# 
# i = 8
# partition_index = 8
# 293 < 99
# 
# i = 9
# partition_index = 8
# 4 < 99
# swap(array, 9, 8)
# partition_index = 9

# Time Complexity: O(n^2) but best and average case is n log(n). This means, this mechanism works if some data is already sorted as space complexity is log(n).
# Space complexity: O(log(n))

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quick_sort(array, left, right):
    length = len(array)
    pivot = 0
    partition_i = 0

    if(left < right):
        pivot = right
        import pdb; pdb.set_trace()
        partition_i = partition_index(array, pivot, left, right)
        import pdb; pdb.set_trace()
        quick_sort(array, left, partition_i - 1)
        quick_sort(array, partition_i + 1, right)
    return array

def partition_index(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    i = left
    while(i<right):
        if(array[i] < pivot_value):
            swap(array, i, partition_index)
            partition_index += 1
        i += 1
    swap(array, right, partition_index)
    return partition_index

def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp

quick_sort(numbers, 0, len(numbers)-1)
print(f'Sorted numbers: {numbers}')
