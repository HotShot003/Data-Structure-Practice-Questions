class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.head = None
    
    def addEledll(self, data):
        t = Node(data)
        
        if self.head is None:
            self.head = t
            return
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        
        curr.next = t
        t.prev = curr

# Example usage
dll = Solution()
dll.addEledll(1)
dll.addEledll(2)
dll.addEledll(3)
dll.addEledll(4)

# Print the list to verify
curr = dll.head
while curr:
    print(curr.data, end=" <-> " if curr.next else "")
    curr = curr.next
