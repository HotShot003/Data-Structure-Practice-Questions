# 1752. Check if Array Is Sorted and Rotated
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Sol 1 : (check array to find arr is sorted or not)

def array(arr,n):
    
    for i in range(n):
        for j in range(1+i,n):
            if arr[i]>arr[j]:
                return False
    return True

arr=[5,1,2,3,4]
n=5        
print(array(arr,n))        

# Sol 2: (main leetcode ans):

class Solution(object):
    def check(self, nums): 
        n = len(nums)
        count = 0    
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                # print(count)
                count += 1
        # return True if count <= 1 else False
        return count == 1
    
nums = [5,4,1,2,3] # it should return false 

print(Solution().check(nums))            
          

# # Sol 3 :
# class Solution(object):
#     def check(self, nums):
#         n = len(nums)
        
#         # Find the break point where the array is not in non-decreasing order
#         for i in range(n - 1):
#             if nums[i] > nums[i + 1]:
#                 # Check if rotating the array at this break point makes it sorted
#                 rotated_sorted = nums[i + 1:] + nums[:i + 1]
                
#                 # Check if rotated_sorted is in non-decreasing order
#                 if all(rotated_sorted[j] <= rotated_sorted[j + 1] for j in range(n - 1)):
#                     return True  # It's sorted and rotated
#                 else:
#                     return False  # It's not possible to make it sorted by rotation
        
#         # If the array is already non-decreasing without any break point
#         return True

# # Test the check method
# nums = [5, 4, 1, 2, 3]
# print(Solution().check(nums))  # Output: False

# # nums = [3, 4, 5, 1, 2]
# # print(Solution().check(nums))  # Output: True
