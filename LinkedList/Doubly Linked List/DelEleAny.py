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

    def printDll(self):
        if self.head is None:
            print('Kuch nhi hai re DLL me')
            return
        
        curr = self.head
        result = []
        
        while curr:
            result.append(curr.data)
            curr = curr.next
        
        print(f'[' + ', '.join(map(str, result)) + ']')
        
    
    def DelEleEnd(self):
        if self.head is None:
            print('Kuch nhi hai re')
            return     
        
        curr = self.head 
        
        while curr.next:
            curr = curr.next
        
        if curr.prev:  # if there is a previous node
            curr.prev.next = None
        else:  # if this is the only node in the list
            self.head = None
        
        curr.prev = None

    def DelEleAny(self, pos=None):
        if pos is None or pos >= self.lenDll():  # default to last position or out of bounds
            pos = self.lenDll() - 1  # default to last position
        
        if pos < 0 or pos == 0:  # If the position is negative or 0, delete the head node
            if self.head is None:
                print('Kuch nhi hai re')
                return
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                return
        
        curr = self.head
        for _ in range(pos):
            curr = curr.next
        
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

# Example usage
s = Solution()
s.AddEleMid(1)
s.AddEleMid(2)
s.AddEleMid(3)

s.printDll()  # Output: [1, 2, 3]

s.DelEleEnd()
s.printDll()  # Output: [1, 2]

s.DelEleAny(0)
s.printDll()  # Output: [2]

s.DelEleAny()
s.printDll()  # Output: Kuch nhi hai re DLL me (or an empty list)

s.AddEleMid(4)
s.AddEleMid(5)
s.printDll()  # Output: [4, 5]

s.DelEleAny(-1)
s.printDll()  # Output: [5]
