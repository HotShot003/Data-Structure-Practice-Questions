# 10. Print Array Size
# 1. You are given a Array.
# 2. You have to return size of array.
# Examples:
# Input:
# arr[N] = {1,2,3,4,5}
# Output:
# 5


def arr(a , index = 0):
    if index == len(a):
        return 0
    return 1 + arr(a , index + 1)


a=[1,2,3,4,5]
print(arr(a))