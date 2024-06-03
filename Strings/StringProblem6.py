# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


# Sol 1 :

def longestCommonPrefix(strs):
    
    if not strs:
        return ""
    
    min_len = min(len(i) for i in strs)
    prefix = ""
    
    for i in range(min_len):
        
        curr_char = strs[0][i]
        
        if all(s[i] == curr_char for s in strs):
            prefix += curr_char
        else:
            break
        
    return prefix

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))     