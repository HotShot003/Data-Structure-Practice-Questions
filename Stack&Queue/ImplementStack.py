# Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 

# Example 1:

# Input: 
# push(2)
# push(3)
# pop()
# push(4) 
# pop()
# Output: 3, 4
# Explanation: 
# push(2)    the stack will be {2}
# push(3)    the stack will be {2 3}
# pop()      poped element will be 3,
#            the stack will be {2}
# push(4)    the stack will be {2 4}
# pop()      poped element will be 4
# Example 2:

# Input: 
# pop()
# push(4)
# push(5)
# pop()
# Output: -1, 5
# Your Task:
# You are required to complete two methods push() and pop(). The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.

# Expected Time Complexity : O(1) for both push() and pop().
# Expected Auixilliary Space : O(1) for both push() and pop().

# Constraints:
# 1 <= Q <= 100
# 1 <= x <= 100


class MyStack:
    
    def __init__(self):
        self.stack = []
        self.top = -1
        
    def push(self,x):
        
        self.top += 1
        if self.top < len(self.stack):
            self.stack[self.top] = x
        else:
            self.stack.append(x)
            
        # if self.stack :
        #     print("True")
        # else :
        #     print("False")    

    def pop(self):
        if self.top == -1:
            return -1
        
        x = self.stack[self.top]
        self.top -= 1
        return x
    
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top + 1):
                print(self.stack[i], end=' ')
            print() 
    
t = MyStack()
t.push(1) 
t.push(2)
t.push(3)
# t.display()          
t.pop() 
t.display()          

            