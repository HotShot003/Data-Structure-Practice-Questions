# 14. Find the first occurence of a element Array
# 1. You are given a Array.
# 2. You have to return the first index of given array elements .
# Examples:
# Input:
# arr[N] = {1,2,3,4,5, 3}
# value = 3
# Output:
# 2


def arr(a,s,index = 0):
    if index == len(a):
        return -1
    
    if s == a[index]:
        return index
    return arr(a,s,index+1)

a=[1,2,3,4,5,3,4]
n=4
print(arr(a,n))