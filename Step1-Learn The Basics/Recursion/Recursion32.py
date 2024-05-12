# 9. Print Array Elements
# 1. You are given a Array of size N.
# 2. You have to Print all the Elements of Array.
# Examples:
# Input:
# arr[N] = {1,2,3,4,5}
# Output:
# 1 2 3 4 5

def print_elements(index=0):
    arr=[1, 2, 3, 4, 5]
    if index < len(arr):
        print(arr[index], end=" ")
        print_elements(index + 1)

# Test the function with your example
print_elements()  # Output: 1 2 3 4 5
