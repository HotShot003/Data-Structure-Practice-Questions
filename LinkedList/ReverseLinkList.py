class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

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
    def lenll(self):
        c = 0
        if self.head is None:
            return c
        curr = self.head
        while curr:
            curr = curr.next
            c += 1
        return c

    def printll(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        curr = self.head
        while curr:
            print(f'{curr.data}', end=' ')
            curr = curr.next
        print()  # Add a newline for better formatting

    def printReverseLL(self):
        def _printReverseLL(node):
            if node is None:
                return
            _printReverseLL(node.next)
            print(f'{node.data}', end=' ')
        
        if self.head is None:
            print("Linked List is Empty")
            return
        
        _printReverseLL(self.head)
        print()  # Add a newline for better formatting

    def reverseLL(self):
        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        self.head = prev
        return self.head

# Function to print the linked list (for testing)
def printLinkedList(head):
    curr = head
    elements = []
    while curr:
        elements.append(curr.data)
        curr = curr.next
    print(" -> ".join(map(str, elements)))

# Create an instance of Solution and add elements
s = Solution()
s.addElementAtPosition(1, 0)
s.addElementAtPosition(2, 1)
s.addElementAtPosition(3, 2)
s.addElementAtPosition(4, 3)

# Print the length of the linked list
print(s.lenll())

# Print the linked list
print("Linked List:")
s.printll()

# Print the linked list in reverse (without modifying it)
print("Reversed Linked List (Print only):")
s.printReverseLL()

# Reverse the linked list (modifies the list)
print("Reversing Linked List (Modify List):")
s.reverseLL()

# Print the reversed linked list
print("Linked List After Reversing:")
s.printll()
