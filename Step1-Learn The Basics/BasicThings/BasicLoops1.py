# Problem statement
# The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

#     F(n) = F(n - 1) + F(n - 2), 
#     Where, F(1) = 1, F(2) = 1


# Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

# "Indexing is start from 1"


# Example :
# Input: 6

# Output: 8

# Explanation: The number is ‘6’ so we have to find the “6th” Fibonacci number.
# So by using the given formula of the Fibonacci series, we get the series:    
# [ 1, 1, 2, 3, 5, 8, 13, 21]
# So the “6th” element is “8” hence we get the output.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 6


# Sample Output 1:
# 8


# Explanation of sample input 1 :
# The number is ‘6’ so we have to find the “6th” Fibonacci number.
# So by using the given formula of the Fibonacci series, we get the series:    
# [ 1, 1, 2, 3, 5, 8, 13, 21]
# So the “6th” element is “8” hence we get the output.


# Expected time complexity :
# The expected time complexity is O(n).


# Constraints:
# 1 <= 'n' <= 10000     
# Where ‘n’ represents the number for which we have to find its equivalent Fibonacci number.

# Time Limit: 1 second


# <===== Attempted Solution =====>\


# =====> Python Solution :

# Sol 1:

def fibonacci(n: int) -> int:
    n = int(n)  # Convert input to integer if it's not already
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    fib_prev = 1
    fib_curr = 1
    
    for _ in range(3, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr

# # Example usage:
n = int(input())  # Ensure input is converted to integer
print(fibonacci(n))  # Output: Fibonacci number for the given input


# Sol 2 :

# def fibonacci(n: int) -> int:
#     if n <= 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# user_input = input()
# n = int(user_input)

