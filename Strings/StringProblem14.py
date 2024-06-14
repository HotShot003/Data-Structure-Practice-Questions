# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3

 

# Constraints:

# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.
# Maximum Nesting Depth Of Parenthesis :


# Sol 1 : Using Loops 

def maxdepth(s):
    # Initialize current depth, maximum depth, and length of the string
    c, m, n = 0, 0, len(s)
    
    for i in range(n):
        if s[i] == '(':
            c += 1
            m = max(c, m)
        elif s[i] == ')':
            c -= 1
            
    return m

# Test case
s = "()(())((()()))"
print(maxdepth(s))  # Output: 3



# Sol 2 : Using Recursion :

def helper(s,index,c,m):
    if index == len(s):
        return m
    if s[index] == '(':
        c += 1
        m = max(c, m)
    elif s[index] == ')':
        c -= 1
    return helper(s,index+1,c,m)

def maxdepth1(s):
    return helper(s,0,0,0)

# Test case
s = "()(())((()()))"
print(maxdepth1(s))  # Output: 3

    
