# Bubble sort
# Time complexity: O(n^2)
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

numbers = [23,43,21,2,3,56,99,]
bubble_sort(numbers)
print(f'Sorted numbers: {numbers}')
