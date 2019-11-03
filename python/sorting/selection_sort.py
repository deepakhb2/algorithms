# Selection Sort
# Time Complexity: O(n^2)
def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_i = i
        for j in range(i+1, length):
            if(arr[min_i] > arr[j]):
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

numbers = [23,43,21,2,3,56,99,]
selection_sort(numbers)
print(f'Sorted numbers: {numbers}')
