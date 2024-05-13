# 15. Find the Last occurence of a element Array
# 1. You are given a Array.
# 2. You have to return the last index of given array elements .
# Examples:
# Input:
# arr[N] = {1,2,3,4,5,3}
# value = 3
# Output:
# 5


def find_last_occurrence(arr, value, index=-1):
    if not arr:
        return -1 if index == -1 else index
    if arr[-1] == value:
        return len(arr) - 1
    return find_last_occurrence(arr[:-1], value, index)

# Test the function
arr = [1, 2, 3, 4, 5, 3]
value = 2
# print(arr[:-1],arr[-1])
print(find_last_occurrence(arr, value))  # Output: 5
