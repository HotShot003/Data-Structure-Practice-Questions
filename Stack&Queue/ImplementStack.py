# Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 

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

            