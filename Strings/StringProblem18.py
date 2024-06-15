# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Sol :

def longestSubstring(s):
    def expand(l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
    res = ""
    
    for i in range(len(s)):
        sub1 = expand(i,i)
        if len(sub1) > len(res):
            res = sub1
        sub2 = expand(i,i+1)
        if len(sub2) > len(res):
            res = sub2 
    return res
s = "cbbd"

print(longestSubstring(s))               
        
        