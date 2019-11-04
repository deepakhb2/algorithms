# Insertion Sort
# Time complexity: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

numbers = [23,43,21,2,3,56,99,283]
insertion_sort(numbers)
print(f'Sorted numbers: {numbers}')
