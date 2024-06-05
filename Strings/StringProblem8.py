# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

# Longest Palindrome :

def longestPalindrome(s):
    hashcount = {}
    
    for i in s :
        if i in hashcount :
            hashcount[i] += 1
        else :
            hashcount[i] = 1
    length = 0
    odd = 0
    
    for count in hashcount.values():
        
        if count % 2 == 0 :
            length += count
        else :
            length += count - 1
            odd += 1
    
    if odd:
        length+=1
    
    return length


s = "abccccdd" 
print(longestPalindrome(s))           