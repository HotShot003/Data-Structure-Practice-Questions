# 4. Factorial
# 1. You are given a positive number n.
# 2. You are required to calculate the factorial of the number.
# 3. You are required to not use any loops.
# Examples:
# Input : 5
# Output : 120


def factorial(n):
    
    if n in [1,0] :
        return 1
    return n * factorial(n-1)

print(factorial(5))