# 8. Array Insertion
# 1. You are given a Empty Array of size N.
# 2. You have to Insert Elements in Array.
# Examples:
# Input:
# arr[N]
# Output:
# 1 2 3 4 5

def create_array(n):
    if n == 0:
        return []
    else:
        arr = create_array(n-1)
        arr.append(n)
        return arr

# Test the function with your example
print(create_array(5))  # Output: [1, 2, 3, 4, 5]


## Manually add elements :

# def add_elements(n, capacity, arr=None):
#     if arr is None:
#         arr = []
#     if len(arr) < capacity and n > 0:
#         element = int(input("Enter element: "))
#         arr.append(element)
#         return add_elements(n-1, capacity, arr)
#     elif len(arr) == capacity or n == 0:
#         return arr
#     else:
#         return 0

# # Test the function with your example
# print(add_elements(5, 10))  # It will ask for 5 inputs and add them to the array
