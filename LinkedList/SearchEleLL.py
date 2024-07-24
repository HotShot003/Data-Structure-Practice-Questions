class Node :
    
    def __init__(s,data):
        
        s.data = data
        s.next = None
        

class Solution :
    
    def __init__(s):
        s.head = None
        
    
    def addEleEnd(s,data):
        
        t = Node(data)
        
        if s.head == None :
            s.head = t
            return s.head
        
        curr = s.head
        
        while curr.next :
            curr = curr.next
        
        curr.next = t
        
        return s.head    
    
    
    def searchEle(s,key):
        
        if s.head is None :
            return False
        
        curr  =  s.head
        
        while curr.next :
            if curr.next.data == key :
                return True
            curr = curr.next
        return False    
    
    
s = Solution()

s.addEleEnd(1)    
s.addEleEnd(2)    
s.addEleEnd(0)

print(s.searchEle(0))