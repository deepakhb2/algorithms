# Reverse string

# Time complexity: O(n)
def reverse_recursive(str):
    str_len = len(str)
    if(str_len == 1):
        return str
    sub_str = str[:str_len-1]
    return str[str_len-1] + reverse_recursive(sub_str)

# Time complexity: O(n)
def reverse_iterative(str):
    reverse_str = ""
    str_len = len(str)
    if(str_len == 1):
        return str
    i = str_len-1
    while(i>=0):
        reverse_str += str[i]
        i -= 1
    return reverse_str

print(f'Iterative: {reverse_iterative("Deepak")}')
print(f'Recursive: {reverse_recursive("Deepak")}')
