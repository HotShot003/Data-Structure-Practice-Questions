# Delete Node At End :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None 

    def addElementll(self, data):
        t = Node(data)
        if not self.head:
            self.head = t
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = t
        
        return self.head

    def deleteElell(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None
    
    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Adding elements to the linked list
    sol.addElementll(1)
    sol.addElementll(2)
    sol.addElementll(3)
    sol.addElementll(4)
    sol.addElementll(5)
    sol.addElementll(6)


    print("Original LinkedList:")
    sol.printLinkedList()
    
    # Deleting the last element
    sol.deleteElell()

    print("LinkedList after deleting the last element:")
    sol.printLinkedList()
