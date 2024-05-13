# 16. Given an array, compute recursively the number of times that the
# value 5 appears in the array
# Examples:
# Input:
# arr[N] = {1,2,3,4,5,3,5,5,5}
# value = 3
# Output:
# 4

def count_occurrences(arr, value):
    if not arr:
        return 0
    return (arr[0] == value) + count_occurrences(arr[1:], value)

# Test the function
arr = [2,1,1,5,5,5,5]
value = 5
print(count_occurrences(arr, value))  # Output: 4
