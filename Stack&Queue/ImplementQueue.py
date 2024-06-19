# Implement a Queue using an Array. Queries in the Queue are of the following type:
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop element from queue and print the poped element)

# Examples:

# Input:
# Q = 5
# Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation:
# In the first test case for query 
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the 
#     queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3 
# Input:
# Q = 4
# Queries = 1 3 2 2 1 4   
# Output: 3 -1
# Explanation:
# In the second testcase for query 
# 1 3 the queue will be {3}
# 2   poped element will be 3 the
#     queue will be empty
# 2   there is no element in the
#     queue and hence -1
# 1 4 the queue will be {4}. 
 

# Expected Time Complexity: O(1) for both push() and pop().
# Expected Auxiliary Space: O(1) for both push() and pop().

# Constraints:
# 1 ≤ Q ≤ 105
# 0 ≤ x ≤ 105



class MyQueue:
    
    def __init__(self,max_size=10):
        self.max_size = max_size
        self.f = 0
        self.r = 0
        self.size = 0
        self.queue = [None] * max_size
    
    def push(self,x):
        
        if self.size == self.max_size:
            raise OverflowError("Pura Bhara Hai Re")
        
        self.queue[self.r] = x
        self.r = (self.r + 1) % self.max_size
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return -1
        
        temp = self.queue[self.f]
        self.f = (self.f + 1) % self.max_size
        self.size -= 1
        return temp
    
    def display(self):
        
        for i in range(self.size):
            print(self.queue[(self.f + i) % self.max_size],end=" ")
        print()    
            
    
t = MyQueue()

t.push(5)
t.push(2)    
t.push(3)
t.push(4)  
t.display()
print(t.pop())
t.display()