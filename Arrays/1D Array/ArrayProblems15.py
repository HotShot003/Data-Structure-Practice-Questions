# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Sol 1:

def sortColors(nums):
        
    r=b=w=0
    for i in nums :

        if i == 0:
            r +=1
        elif i == 1:
            w+=1
        elif i == 2:
            b+=1

    for i in range(r):
        nums[i] = 0

    for i in range(r, r + w):
        nums[i] = 1

    for i in range(r+w, len(nums)):
        nums[i] = 2
        
    return nums    

print(sortColors([[2,0,2,1,1,0]]))



# Sol 2 : Dutch National Flag Algorithm

def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
# print("After sorting:")
for num in arr:
    print(num, end=" ")
print()



