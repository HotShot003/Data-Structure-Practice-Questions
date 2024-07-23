# Define the Node and Solution classes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class Solution:
#     def __init__(self):
#         self.head = None

#     def addElementll(self, data):
#         t = Node(data)
        
#         if self.head is None:
#             self.head = t
#             return self.head
        
#         t.next = self.head
#         self.head = t
#         return self.head

#     def addElementAtPosition(self, data, position):
#         t = Node(data)
        
#         # Special case for inserting at the head (position 0)
#         if position == 0:
#             t.next = self.head
#             self.head = t
#             return self.head
        
#         # Traverse to the node just before the insertion point
#         curr = self.head
#         for _ in range(position - 1):
#             if curr is None:
#                 print("Position out of bounds")
#                 return self.head
#             curr = curr.next
        
#         # Special case for inserting at the end of the list
#         if curr is None:
#             print("Position out of bounds")
#             return self.head
        
#         # Insert the new node
#         t.next = curr.next
#         curr.next = t
        
#         return self.head

# # Function to print the linked list
# def printLinkedList(head):
#     curr = head
#     elements = []
#     while curr:
#         elements.append(curr.data)
#         curr = curr.next
#     print(" -> ".join(map(str, elements)))

# # Create an instance of Solution
# sol = Solution()

# # Adding elements and printing the list after each operation
# print("Adding 1 to the list:")
# sol.addElementll(1)
# printLinkedList(sol.head)

# print("Adding 2 to the list:")
# sol.addElementll(2)
# printLinkedList(sol.head)

# print("Adding 3 to the list:")
# sol.addElementll(3)
# printLinkedList(sol.head)

# print("Inserting 4 at position 1:")
# sol.addElementAtPosition(4, 1)
# printLinkedList(sol.head)

# print("Inserting 5 at position 3:")
# sol.addElementAtPosition(5, 3)
# printLinkedList(sol.head)

# print("Inserting 6 at position 0:")
# sol.addElementAtPosition(6, 0)
# printLinkedList(sol.head)

# print("Trying to insert at an out-of-bounds position (e.g., 10):")
# sol.addElementAtPosition(7, 10)
# printLinkedList(sol.head)


class solution :
    
    def __init__(s) :
        s.head = None 
        
    
    def addele(s,head,pos):
        
        t = Node()
        
        if s.head == None :
            s.head = t
            
            return    