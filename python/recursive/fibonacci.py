import time
# Given a number N return the index value of the Fibonacci sequence where the sequence is :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ....
# The pattern of the sequence is that each value is the sum of the 2 previous values.

# Time complexity: O(n-2) = O(n) Linear time
# Space  complexity: O(n)
def fibonacci_iterative(num):
    fib = [0, 1]
    for i in range(2, num + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[num]

# Time complexity: O(2^n)
def fibonacci_recursive(num):
    if(num < 2):
        return num
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

i_start = time.process_time()
print(f"Iterative value: {fibonacci_iterative(30)}")
print(f"Time taken: {time.process_time() - i_start}")
r_start = time.process_time()
print(f"Recursive value: {fibonacci_recursive(30)}")
print(f"Time taken: {time.process_time() - r_start}")
