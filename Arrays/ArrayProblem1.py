# Given an array A[] of size n. The task is to find the largest element in it.
 

# Example 1:

# Input:
# n = 5
# A[] = {1, 8, 7, 56, 90}
# Output:
# 90
# Explanation:
# The largest element of given array is 90.
 

# Example 2:

# Input:
# n = 7
# A[] = {1, 2, 0, 3, 2, 4, 5}
# Output:
# 5
# Explanation:
# The largest element of given array is 5.
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function largest() which takes the array A[] and its size n as inputs and returns the maximum element in the array.

 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

 

# Constraints:
# 1 <= n<= 103
# 0 <= A[i] <= 103
# Array may contain duplicate elements. 

# Sol 1: (Using Linear Search with Loops)
    
def Array(arr,n):
    
    max_num = arr[0]
    
    for i in range(1,n):
        
        if max_num < arr[i]:
            max_num = arr[i]
    return max_num


arr=[1,2,3,4,5]
n=5
print(Array(arr,n))        

# Sol 2: (Using Recursion)

def Array1(arr,n,max=arr[0],index=1):
    
    if n == index:
        return max
    
    if max < arr[index]:
        max = arr[index]
    return Array1(arr,n,max,index+1)    


arr=[1,2,3,4,5]
n=5
print(Array1(arr,n))    
    
    