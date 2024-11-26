# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

class MyQueue:
    
    def __init__(s):
        
        s.s1 = []
        s.s2 = []
    
    
    def push(s,x):
        s.s1.append(x)
        
    
    def pop(s):
        if not s.s2:
            while s.s1:
                s.s2.append(s.s1.pop())
    
        return s.s2.pop()
    
    def peek(s):
        if not s.s2:
            while s.s1:
                s.s2.append(s.s1.pop())
    
        return s.s2[-1]
    
    def empty(s):
        return not s.s2 and not s.s1                  
    
myQueue=MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.peek())
print(myQueue.empty())
print(myQueue.pop())
print(myQueue.empty()) 
