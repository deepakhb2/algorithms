# 5! = 5 * 4 * 3 * 2 * 1

# Find factorial using recursive method.
# base case: return 1 if number is 1
# recursive case: call recursive method if number is greater than 1.
# Time complexity is: O(n)
def find_factorial_recursive(number):
    if(number == 2):
        return 2
    return number * find_factorial_recursive(number-1)

# Find factorial using iterative method.
# Time complexity is: O(n)
def find_factorial_iterative(number):
    result = 1
    if(number == 2):
        return 2
    for num in range(2, number+1):
        result = result * num
    return result

print(f"Recursive value: {find_factorial_recursive(5)}")
print(f"Iterative value: {find_factorial_iterative(5)}")
