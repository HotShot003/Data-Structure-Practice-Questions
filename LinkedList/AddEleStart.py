# Define the Node and Solution classes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def addElementll(self, data):
        t = Node(data)
        
        # Handle case where the list is empty
        if self.head is None:
            self.head = t
            return self.head
        
        # Handle case where the list is not empty
        t.next = self.head
        self.head = t

        return self.head

# Function to print the linked list
def printLinkedList(head):
    curr = head
    elements = []
    while curr:
        elements.append(curr.data)
        curr = curr.next
    print(" -> ".join(map(str, elements)))

# Create an instance of Solution
sol = Solution()

# Adding elements and printing the list after each operation
print("Adding 1 to the list:")
head = sol.addElementll(1)
printLinkedList(head)

print("Adding 2 to the list:")
head = sol.addElementll(2)
printLinkedList(head)

print("Adding 3 to the list:")
head = sol.addElementll(3)
printLinkedList(head)
