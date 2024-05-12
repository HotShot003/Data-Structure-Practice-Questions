# 11. Print array elements in reverse order
# 1. You are given a Array.
# 2. You have to print array elements in reverse order.
# Examples:
# Input:
# arr[N] = {1,2,3,4,5}
# Output:
# 5 4 3 2 1


def print_elements(index=0):
    arr=[1, 2, 3, 4, 5]
    if index < len(arr):
        print_elements(index + 1)
        print(arr[index], end=" ")

# Test the function with your example
print_elements()  # Output: 5 4 3 2 1
