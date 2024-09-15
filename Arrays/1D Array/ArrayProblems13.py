#  Subarray sum == k 

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

def SubarraySum(nums,k):
    
        dic = {0:1}
        n=len(nums)
        c = 0
        s = 0

        for i in nums:
            s+=i
            if s-k in dic:
                c+=dic[s-k]
            if s in dic:
                dic[s] += 1
            else :
                dic[s] = 1         

        return c
                     
arr=[1,2,3,4,5,6]
k = 6
print(SubarraySum(arr,k))
