# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False



# Sol 1 :

class MyQueue:
    
    def __init__(self):
        self.item = []
    
    def push(self,x):
        self.item.append(x)
    
    def pop(self):
        if not self.empty():
            return self.item.pop(0)
        
    def peek(self):
        if not self.empty():
            return self.item[0]
    
    def empty(self):
        return len(self.item) == 0 
    
    def size(self):
        return len(self.item)

class MyStack:
    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()
    
    def push(self,x):
        self.q1.push(x)
    
    def empty(self):
        return self.q1.empty() 
    
    def pop(self):
        while self.q1.size() > 1:
            self.q2.push(self.q1.pop())
        
        top = self.q1.pop()
        self.q1,self.q2 = self.q2,self.q1
        
        return top
    
    def top(self):
        while self.q1.size() > 1:
            self.q2.push(self.q1.pop())
        
        top = self.q1.peek()
        self.q2.push(self.q1.pop()) 
        self.q1,self.q2 = self.q2,self.q1
        
        return top
    
# Testing // 
    
def test_my_stack():
    stack = MyStack()
    
    # Test case 1: Check if the stack is initially empty
    assert stack.empty() == True, "Test case 1 failed: Stack should be empty initially"
    
    # Test case 2: Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    # Test case 3: Check the top element
    assert stack.top() == 3, "Test case 3 failed: Top element should be 3"
    
    # Test case 4: Pop the top element
    assert stack.pop() == 3, "Test case 4 failed: Popped element should be 3"
    
    # Test case 5: Check the top element after pop
    assert stack.top() == 2, "Test case 5 failed: Top element should be 2"
    
    # Test case 6: Pop all elements and check if stack is empty
    assert stack.pop() == 2, "Test case 6 failed: Popped element should be 2"
    assert stack.pop() == 1, "Test case 6 failed: Popped element should be 1"
    assert stack.empty() == True, "Test case 6 failed: Stack should be empty after popping all elements"
    
    print("All test cases passed!")

# Run the tests
test_my_stack()
