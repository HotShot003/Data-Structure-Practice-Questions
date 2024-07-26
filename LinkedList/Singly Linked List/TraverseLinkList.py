class Node :
    
    def __init__(s,data):
        s.data = data
        s.next = None
        

class Solution :
    
    def __init__(s):
        s.head = None
        
    def addElementAtPosition(self, data, position):
        t = Node(data)
        
        # Special case for inserting at the head (position 0)
        if position == 0:
            t.next = self.head
            self.head = t
            return self.head
        
        # Traverse to the node just before the insertion point
        curr = self.head
        for _ in range(position - 1):
            if curr is None:
                print("Position out of bounds")
                return self.head
            curr = curr.next
        
        # Special case for inserting at the end of the list
        if curr is None:
            print("Position out of bounds")
            return self.head
        
        # Insert the new node
        t.next = curr.next
        curr.next = t
        
        return self.head     
    
    
    # Count Length Of Linked List
    def lenll(s):
        
        c = 0
        
        if s.head is None :
            return c   
        
        curr = s.head 
        
        while curr :
            curr = curr.next
            c+=1
        
        return c
    
    def printll(s):
        
        if s.head == None :
            print("Linked List is Empty")
            return
        
        curr = s.head 
        
        while curr :
            print(f'{curr.data}',end=' ')
            # print(curr.data,end=" ")
            curr = curr.next
            # print()
            
            
    
s = Solution()

s.addElementAtPosition(1,0)    
s.addElementAtPosition(2,1)    
print(s.lenll())
s.printll()

