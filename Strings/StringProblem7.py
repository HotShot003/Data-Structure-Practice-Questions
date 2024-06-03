# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
# Isomorphic Strings :

def IsomorphicString(s,t):
    
    if len(s) != len(t):
        return False
    
    hash_s_t  = {}
    hash_t_s = {}
    
    
    for c_s,c_t in zip(s,t):
        
        if c_s in hash_s_t:
            if hash_s_t[c_s] != c_t:
                return False
        else:
            hash_s_t[c_s] = c_t
        
        if c_t in hash_t_s:
            if hash_t_s[c_t] != c_s:
                return False
        else:
            hash_t_s[c_t] = c_s
    return True

s='egg'
t='ade'
print(IsomorphicString(s,t))            