# You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

# Example:

# Input: 
# *-A/BC-/AKL
# Output: 
# ABC/-AK/L-*
# Explanation: 
# The above output is its valid postfix form.
# Your Task:

# Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.

 

# Expected Time Complexity: O(N).

# Expected Auxiliary Space: O(N).

# Constraints:

# 3<=pre_exp.length()<=100

def preToPost(rep):
    stack = []
    
    op = set(['+','-','/','*'])
    
    for i in reversed(rep):
        
        if i in op:
            op1 = stack.pop()
            op2 = stack.pop()
        
            post = op1 + op2 + i
            stack.append(post)
        else :
            stack.append(i)
            
    return stack[-1]            

print(preToPost(rep='*AB'))
