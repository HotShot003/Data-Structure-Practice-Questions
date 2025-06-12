# 2. Longest Palindromic Substring
# Problem: Given a string of lowercase English letters, find the length of the longest substring that is a palindrome.
# Example:  
# Input: str = "babad"  

# Output: 3 (e.g., "bab" or "aba")



s = str(input())

def pali(s):
    n = len(s)
    max_l = 1
    
    for i in range(n):
        
        l,r = 1,1
        
        while l>=0 and r < n and s[l] == s[r]:
            max_l = max(max_l,r-l+1) 
            l-=1
            r+=1
        
        l,r = 1,1+1
        
        while l>=0 and r < n and s[l] == s[r]:
            max_l = max(max_l,r-l+1) 
            l-=1
            r+=1    
            
    return max_l

print(pali(s))