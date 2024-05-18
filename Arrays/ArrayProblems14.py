# Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

 

# Example 1:
 

# Input :
# A[] = {10, 5, 2, 7, 1, 9}
# K = 15
# Output : 4
# Explanation:
# The sub-array is {5, 2, 7, 1}.
# Example 2:

# Input : 
# A[] = {-1, 2, 3}
# K = 6
# Output : 0
# Explanation: 
# There is no such sub-array with sum 6.
# Your Task:
# This is a function problem. The input is already taken care of by the driver code. You only need to complete the function lenOfLongSubarr() that takes an array (A), sizeOfArray (n),  sum (K)and returns the required length of the longest Sub-Array. The driver code takes care of the printing.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

 

# Constraints:
# 1<=N<=105
# -105<=A[i], K<=105


# Longest SubArray :


arr = [1,2,3,4,5,6]
k=3

def longsubarr(arr,k):
    
    preSumMap = {}
    sum = 0
    maxLen = 0
    
    for i in range(len(arr)):
        sum += arr[i]
        
        if sum == k :
            maxLen = i+1
        
        rem = sum - k
        
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen,length)     
        
        if sum not in preSumMap:
            preSumMap[sum] = i    
    return maxLen
# arr=[1,0,0,3]
# k=2
arr=[-1,1,1]
k=1
print(longsubarr(arr,k))        
