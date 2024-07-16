# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105



def trapped(height):
    
    if not height :
        return 0
    
    left = 0
    right = len(height) - 1 
    
    right_max,left_max = 0,0
    
    water_trapped = 0
    
    while left < right :
        
        if height[left] < height[right]:
            
            if height[left] >= left_max:
                left_max = height[left]
            
            else :
                water_trapped += left_max - height[left]

            left += 1
            
        else :
            if height[right] >= right_max:
                right_max = height[right]
            
            else :
                water_trapped += right_max - height[right]
            right -= 1    
    return water_trapped


print(trapped(height=[4,2,0,3,2,5]))            