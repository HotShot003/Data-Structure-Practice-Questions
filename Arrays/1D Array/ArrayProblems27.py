# Count Subarray sum Equals K
# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements within an array.


# Sol 1: O(n2)

def subarray(arr,k):
    
    c = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i,n):
            
            sum1 = sum(arr[i:j+1])
        
            if sum1 == k:
                c+=1
    return c

arr =[1,2,3,4,5]
k=3
# print(subarray(arr,k))            


# Sol 2 : 
# O(n2) time and O(n) space

def subarray1(arr,k):
    c = 0
    n = len(arr)
    
    for i in range(n):
        sum2=0
        for j in range(i,n):
            sum2 += arr[j]
            
            if sum2 == k:
                c+=1
    return c

arr =[1,2,3,4,5]
k=3
# print(subarray1(arr,k))            

# Sol 3:

def subarray2(arr, k):
    # Dictionary to store the frequency of prefix sums
    dic = dict()
    # Initialize with 0 sum having one frequency
    dic[0] = 1
    
    n = len(arr)
    presum = 0
    c = 0
    
    for i in range(n):
        # Add current element to prefix sum
        presum += arr[i]
        
        # Calculate the required prefix sum to find the subarray with sum k
        rem = presum - k
        
        # If the required prefix sum is found in the dictionary, 
        # it means there are dic[rem] subarrays ending at current index with sum k
        if rem in dic:
            c += dic[rem]
        
        # Update the frequency of the current prefix sum in the dictionary
        if presum in dic:
            dic[presum] += 1
        else:
            dic[presum] = 1
    
    return c

# Test the function
arr = [3,-3,1,1,1]
k = 3
print(subarray2(arr, k))  # Output should be 2


