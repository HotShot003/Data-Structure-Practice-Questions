# You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

# Example 1:

# Input: 
# *-A/BC-/AKL
# Output: 
# ((A-(B/C))*((A/K)-L))
# Explanation: 
# The above output is its valid infix form.
# Your Task:

# Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

 

# Expected Time Complexity: O(N).

# Expected Auxiliary Space: O(N).

# Constraints:

# 3<=|S|<=104

def PrefixTOInfix(plain):
    
    stk = []
    op = set(['+','-','/','*'])
    
    
    for ch in reversed(plain):
        if ch in op:
            op1 = stk.pop()
            op2 = stk.pop()
            
            new_plain = "{}{}{}".format(op1,ch,op2)
            stk.append(new_plain)
        
        else :
            stk.append(ch)
    
    return stk[0]

print(PrefixTOInfix(plain='+AB'))            