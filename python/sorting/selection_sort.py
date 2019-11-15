# Selection Sort
# Time Complexity: O(n^2)
# In each loop select the smallest item and swap the value to first index. Than repeat the steps and swap the value with second index. This continues

def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_i = i
        for j in range(i+1, length):
            if(arr[min_i] > arr[j]):
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

numbers = [23,43,21,2,3,56,99,80]
selection_sort(numbers)
print(f'Sorted numbers: {numbers}')
