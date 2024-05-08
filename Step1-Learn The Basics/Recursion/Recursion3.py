# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self,s):
        def isAlphanumeric(char):
            return char.isalnum()
        
        def isPalindromeRecursion(left, right):
            
            if left >= right:
                return True
            
            while left < right and not isAlphanumeric(s[left]):
                left+=1
            
            while left < right and not isAlphanumeric(s[right]):
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            return isPalindromeRecursion(left+1,right-1)
        
        return isPalindromeRecursion(0,len(s) - 1)
    
    
sol = Solution()

s1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s1))  # Output: True

s2 = "race a car"
print(sol.isPalindrome(s2))  # Output: False

s3 = " "
print(sol.isPalindrome(s3))  # Output: True