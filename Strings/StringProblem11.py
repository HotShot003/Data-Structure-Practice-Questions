# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


def stringsAnagram(s,t):
    
    if len(s) != len(t):
        return False
    
    c_s = {}
    c_t = {}
    
    for i in s:
        if i in c_s:
            c_s[i] += 1
        else:
            c_s[i] = 1
    
    for i in t :
        if i in c_t:
            c_t[i] += 1
        else:
            c_t[i] = 1
    return c_s == c_t

s = "anagram"
t = "nagaram"    
print(stringsAnagram(s,t))    