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
