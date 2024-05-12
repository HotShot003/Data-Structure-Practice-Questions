# 12. Find the kth element of Array
# 1. You are given a Array.
# 2. You have to print kth array elements .
# Examples:
# Input:
# arr[N] = {1,2,3,4,5}
# k = 3
# Output:
# 4


def get_element(arr, index=0):
    if index < len(arr):
        return arr[index]
    else:
        return "Index out of range"

# Test the function with your example
print(get_element([1, 2, 3, 4, 5], 2))  # Output: 3
