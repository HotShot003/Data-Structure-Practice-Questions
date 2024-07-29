class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.head = None

    def lenDll(self):
        c = 0
        temp = self.head
        while temp:
            c += 1
            temp = temp.next
        return c
    
    def AddEleMid(self, data, pos=None):
        t = Node(data)
        
        if pos is None:  # Default case, add at the end
            pos = self.lenDll()
        
        if pos <= 0:  # If position is 0 or negative, add at the start
            if self.head is None:
                self.head = t
            else:
                t.next = self.head
                self.head.prev = t
                self.head = t
            return
        
        curr = self.head
        l = self.lenDll()
        
        if pos >= l:  # If position is greater than length, add at the end
            if self.head is None:
                self.head = t
                return
            while curr.next:
                curr = curr.next
            curr.next = t
            t.prev = curr
            return
        
        # For all other positions, add in the middle
        for i in range(pos-1):
            curr = curr.next
        
        t.next = curr.next
        if curr.next:
            curr.next.prev = t
        curr.next = t
        t.prev = curr
        return s.head
    
    def ReversedDLL(s):
        
        if s.head == None :
            return None 
        
        curr = s.head
        temp = None
        
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        
        if temp :
            s.head = temp.prev
        return s.head
            
    
    def printDll(self):
        if self.head is None:
            return 'Kuch nhi hai re DLL me'
        
        curr = self.head
        result = []
        
        while curr:
            result.append(curr.data)
            curr = curr.next
        
        print(f'[' + ', '.join(map(str, result)) + ']')
        
# Example usage
s = Solution()
s.AddEleMid(1)
s.AddEleMid(2)
s.AddEleMid(10)
s.AddEleMid(3, 1)  # Add 3 at position 1
s.AddEleMid(4, -1) # Add 4 at the start due to negative position
s.AddEleMid(5, 10) # Add 5 at the end due to position greater than length
s.AddEleMid(6)     # Add 6 at the end by default

print('Before Reverse ')
s.printDll()

print('After Reversed ')
s.ReversedDLL()
s.printDll()