# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

# Example 1:

# Input:
# S = "aba", K = 2
# Output:
# 3
# Explanation:
# The substrings are: "ab", "ba" and "aba".
# Example 2:

# Input: 
# S = "abaaca", K = 1
# Output:
# 7
# Explanation:
# The substrings are: "a", "b", "a", "aa", "a", "c", "a". 
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function substrCount() which takes the string S and an integer K as inputs and returns the number of substrings having exactly K distinct characters.

# Expected Time Complexity: O(|S|).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 ≤ |S| ≤ 106
# 1 ≤ K ≤ 26

def substrCount(s, k):
    def countAtMostKDistinct(s, k):
        char_count = {}
        left = 0
        result = 0
        distinct_count = 0
        
        for right in range(len(s)):
            if s[right] not in char_count or char_count[s[right]] == 0:
                distinct_count += 1
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while distinct_count > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    distinct_count -= 1
                left += 1
            
            result += right - left + 1
        
        return result
    
    return countAtMostKDistinct(s, k) - countAtMostKDistinct(s, k - 1)

# Test cases
print(substrCount("aba", 2))  # Output: 3
print(substrCount("abaaca", 1))  # Output: 7
