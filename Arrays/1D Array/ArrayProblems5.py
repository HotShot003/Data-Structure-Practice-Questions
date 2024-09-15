# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


# First Left Rotate by 1:

def array1(arr):
    
    temp = arr[0]
    
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp    
    return arr
arr=[1,2,3,4,5]
print(array1(arr))    


# For n time Left Rotated:


def array2(arr,n):
    n = n % len(arr)
    
    for j in range(n):
        temp = arr[0]
        for i in range(1,len(arr)):
            arr[i-1] = arr[i]
        arr[len(arr)-1] = temp    
    return arr

arr=[1,2,3,4,5,6,7]
n=3
print(array2(arr,n))  


# Optimised Left Rotate :

def LeftRotate(nums,k):  
    n = len(nums)
    k = k % n
    nums[:] = nums[k:] + nums[:k]
    return nums
k=3
# print()
nums=[1,2,3,4,5,6,7]
# print(nums[:] ,nums[len(nums)-k:], nums[:len(nums)-k])
# print()
print('left rotate',LeftRotate(nums,k))


# First right rotate by 1:

def rightRotate1(arr):
    temp = arr[-1]
    
    for i in range(1,len(arr)):
        arr[len(arr)-i] =arr[len(arr)-(i+1)]
    arr[0] = temp
    return arr

arr=[1,2,3,4,5]
print(rightRotate1(arr))


# Right Rotate by n :

def rightRotate2(arr,n):
    
    n = n % len(arr)
    for j in range(n):
        temp = arr[-1]
        
        for i in range(1,len(arr)):
            arr[len(arr)-i] =arr[len(arr)-(i+1)]
        arr[0] = temp
    return arr

arr=[1,2,3,4,5]
n=3
print(rightRotate2(arr,n))


# Best optimise Solution FOr Right Rotate :


def rightRotate3(nums,k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
nums=[1,2,3,4,5]
k=3    
print(rightRotate3(nums,k))    
# print()
# nums=[1,2,3,4,5]
# print(nums[:] ,nums[len(nums)-k:], nums[:len(nums)-k])