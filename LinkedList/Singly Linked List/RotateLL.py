# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None 
    
    def add_element(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        
        curr.next = new_node    
        
        return self.head
    
    def rotateRight(self, k):
        if not self.head or not self.head.next or k == 0:
            return self.head

        # Step 1: Find the length of the list and the last node
        length = 1
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            length += 1

        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return self.head

        # Step 3: Find the new tail: (length - k - 1)th node
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Set the new head and rotate the list
        new_head = new_tail.next
        new_tail.next = None
        last_node.next = self.head
        self.head = new_head
        
        return self.head

    def print_linkedlist(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next


# Example usage:
s = Solution()

# Add elements to the linked list
s.add_element(1)
s.add_element(2)
s.add_element(3)
s.add_element(4)
s.add_element(5)

print("Original list:")
s.print_linkedlist()

# Rotate the list by 2 places
s.rotateRight(2)

print("Rotated list by 2 places:")
s.print_linkedlist()

# Another example
s2 = Solution()
s2.add_element(0)
s2.add_element(1)
s2.add_element(2)

print("Original list:")
s2.print_linkedlist()

# Rotate the list by 4 places
s2.rotateRight(4)

print("Rotated list by 4 places:")
s2.print_linkedlist()