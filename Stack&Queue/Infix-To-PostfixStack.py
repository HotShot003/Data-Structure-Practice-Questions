# Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

# Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
# Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
# Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
# Example 1:

# Input: str = "a+b*(c^d-e)^(f+g*h)-i"
# Output: abcd^e-fgh*+^*+i-
# Explanation:
# After converting the infix expression 
# into postfix expression, the resultant 
# expression will be abcd^e-fgh*+^*+i-
# Example 2:

# Input: str = "A*(B+C)/D"
# Output: ABC+*D/
# Explanation:
# After converting the infix expression 
# into postfix expression, the resultant 
# expression will be ABC+*D/
 
# Your Task:
# This is a function problem. You only need to complete the function infixToPostfix() that takes a string(Infix Expression) as a parameter and returns a string(postfix expression). The printing is done automatically by the driver code.

# Expected Time Complexity: O(|str|).
# Expected Auxiliary Space: O(|str|).

# Constraints:
# 1 ≤ |str| ≤ 105

# S0l : 1

class Solution :
    
    def infixToPostfix(self,exp):
        
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            elif op == '^':
                return 3
            return 0
        
        def is_operator(c):
            return c in '+-*/^'
        
        stk = []
        res = []
        
        for char in exp :
            if char.isalpha():
                res.append(char)
            elif char == '(' :
                stk.append(char)
            elif char == ')':
                while stk and stk[-1] != '(' :
                    res.append(stk.pop())
                stk.pop()
            
            else :
                while stk and precedence(stk[-1]) >= precedence(char):
                    res.append(stk.pop())
                stk.append(char)
            
        while stk :
            res.append(stk.pop())
        
        return "".join(res)


# Example usage:
solution = Solution()
print(solution.infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))  # Output: "abcd^e-fgh*+^*+i-"
print(solution.infixToPostfix("A*(B+C)/D"))              # Output: "ABC+*D/"                    
                    