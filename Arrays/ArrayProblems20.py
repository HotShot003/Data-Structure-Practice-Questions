# # Reaarange array element by Sign 

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
 

# Constraints:

# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.



# Sol 1 : Brute Force

def rearrangeArr(arr):
    pos = []
    neg = []
    
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else :
            neg.append(arr[i])    
    
    for i in range(len(pos)):
        arr[2*i] = pos[i]
    
    for i in range(len(neg)):
        arr[2 * i + 1] = neg[i]    
        
    return arr


arr = [1,-1,-2,2]
print(rearrangeArr(arr))    
               
# Sol 2 : Optimal               

def rearrangeArr1(arr):
    pos , neg = 0 , 1
    
    n=len(arr)
    res=[0] * n
    
    for i in range(n):
        
        if arr[i] < 0:
            res[neg] = arr[i]
            neg+=2
        else :
            res[pos] = arr[i]
            pos+=2
            
    return res        

arr = [1,-2,2]
print(rearrangeArr1(arr))    