# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.


# Sol :

def beautySum(s):
    
    total_beauty = 0
    
    for i in range (len(s)-2):
        freq={}
        
        for j in range(i,len(s)):
            if s[j] in freq:
                freq[s[j]] += 1
            else :
                freq[s[j]] = 1
            
            max_freq = max(freq.values())
            min_freq = min([fre for fre in freq.values() if fre>0])       
            total_beauty += (max_freq-min_freq)
    return total_beauty        
s = "aabcb"
print(beautySum(s))