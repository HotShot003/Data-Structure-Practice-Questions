# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100



class Node :
    
    def __init__(s,data):
        
        s.data = data
        s.next = None


class Solution :
    
    def __init__(s):
        s.head = None
        
    
    def insert(s,data):
        
        t = Node(data)
        
        
        if s.head is None :
            s.head = t
            return
        
        curr = s.head
        while curr.next :
            
            curr=curr.next
            
        curr.next = t
        
        return s.head
    
    def printll(s,start=None):
        
        if start == None:
            start = s.head
        
        if start is None :
            print('Empty')
            return
            
        
        curr = start
        
        while curr :
            
            print(curr.data,end=' ')
            curr = curr.next
        print()
        return

    
    def middle(s):
                
        def lenll(head):
            
            c = 0 
            while head :
                c+=1
                head = head.next
            
            return c    
        
        t = lenll(s.head)   
        
        mid = t // 2
        
        curr = s.head
        
        for _ in range(mid):
            
            curr = curr.next
        
        return curr    
             
        

s = Solution()
s.insert(1)
s.insert(2)
s.insert(3)    
s.insert(4)    
s.insert(5)    
# s.insert(6)    
    
s.printll()

mid_node = s.middle()
s.printll(mid_node)
            
        
        