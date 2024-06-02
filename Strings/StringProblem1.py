# Reverse A String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


# Time Complexity - O(n)
# Space Complexity - O(1)

# Sol 1: Two Pointer Approach

def ReverseString(s):
    s=list(s)
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

s = 'hello'
print(ReverseString(s))    


# Sol 2 : Simple Formula i.e. n-i-1

def ReverseString1(s):
    
    n = len(s)
    
    for i in range(n//2):
        s[i],s[n-i-1] = s[n-i-1] , s[i]
    
    return s

s = ['H','E','L','L','O']
print(ReverseString1(s))


    