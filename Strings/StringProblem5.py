# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

# Example 1:

# Input: s = "coaching", t = "coding"
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
# Example 2:

# Input: s = "abcde", t = "a"
# Output: 0
# Explanation: t is already a subsequence of s ("abcde").
# Example 3:

# Input: s = "z", t = "abcde"
# Output: 5
# Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
# Now, t is a subsequence of s ("zabcde").
# It can be shown that appending any 4 characters to the end of s will never make t a subsequence.


# Sel 1 :

def makeSubsequence(s,t):
    
    s_index = t_index = 0
    s_len=len(s)
    t_len=len(t)
    
    while s_index < s_len and t_index < t_len:
        
        if s[s_index] == t[t_index]:
            t_index += 1
        s_index+=1
    
    return t_len - t_index

s='coaching'
t='coding'
print(makeSubsequence(s,t))        

# Sol 2 :

def makeSubsequence1(s,t):
    
    tlen = len(t)
    j = 0
    
    for i in s :
        if i == t[j]:
            j += 1
            if j == tlen:
                break
    return len(t) - j        

s='coaching'
t='coding'
print(makeSubsequence1(s,t))        
