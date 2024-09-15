# Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

# Example 1:

# Input: 
# N = 6
# Arr[] = {12, 35, 1, 10, 34, 1}
# Output: 34
# Explanation: The largest element of the 
# array is 35 and the second largest element
# is 34.
# Example 2:

# Input: 
# N = 3
# Arr[] = {10, 5, 10}
# Output: 5
# Explanation: The largest element of 
# the array is 10 and the second 
# largest element is 5.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function print2largest() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. If 2nd largest element doesn't exist then return -1.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 2 ≤ N ≤ 105
# 1 ≤ Arri ≤ 105


# Sol 1:
    
def array(arr,n):
    
    if n < 2:
        return -1
    
    fmax = smax = 0
    
    for i in range(n):
        
        if arr[i] > fmax:
            fmax = arr[i]
    
    for i in range(n):
        
        if arr[i] > smax  and arr[i] < fmax:
            smax = arr[i]
    if smax == 0 :
        return -1
    return smax

arr = [1,2,3,4,5]
n=5
print(array(arr,n))        


# Sol 2: Using Recursion

def array1(arr,n,index=0,smax=0,fmax=0):
    
    if index == n :
        return -1 if smax == 0 else smax
    
    if arr[index] > fmax:
        
        fmax , smax = arr[index] , fmax
    
    elif  arr[index] > smax and arr[index] < fmax :
        smax = arr[index]
    
    return array1(arr,n,index+1,smax,fmax)


print(array1(arr,n))      