class Node :
     
    def __init__(s,data):
         
        s.data = data
        s.next = None
        s.prev = None


class Soltuion :
    
    def __init__(s):
        s.head = None
    
    
    def addEleStart(s,data):
        
        t = Node(data)
        
        if s.head is None :
            s.head = t
            return    

        curr = s.head 
        
        t.next = curr
        curr.prev = t
        s.head = t
        
        return s.head
    
    def printll(s):
        
        curr = s.head
        while curr :
            print(curr.data , end=' ')
            curr = curr.next
        print()    

s = Soltuion()

s.addEleStart(1)
s.addEleStart(2)
s.addEleStart(3)

s.printll()
        