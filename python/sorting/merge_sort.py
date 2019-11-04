# Merge Sort
# Time Complexity: O(n*log(n))
# Space Complexity: O(n)
def merge_sort(numbers):
    length = len(numbers)
    if(length <= 1):
        return numbers

    middle = length//2
    left = numbers[:middle]
    right = numbers[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while(left_index < len(left) and right_index < len(right)):
        if(left[left_index] < right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers = merge_sort(numbers)
print(f'Sorted numbers: {numbers}')

# Sorting Logic
# 99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0
# 99, 44, 6, 2, 1  5, 63, 87, 283, 4, 0
# 99, 44  6, 2, 1  5, 63, 87  283, 4, 0
# 99  44  6  2, 1  5  63, 87  283  4, 0
# 99  44  6  2  1  5  63  87  283  4  0
# 99  44  6  1, 2  5  63, 87  283  0, 4
# 44, 99  1, 2, 6  5, 63, 87  0, 4, 283
# 1, 2, 6, 44, 99  0, 4, 5, 63, 87, 283
# 0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283
