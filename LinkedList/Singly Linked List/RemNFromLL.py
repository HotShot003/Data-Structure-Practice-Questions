# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: Node
        :type n: int
        :rtype: Node
        """
        # Create a dummy node that points to the head
        dummy = Node(0)
        dummy.next = head
        first = second = dummy
        
        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both first and second pointers
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        return dummy.next

# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.data)
        current = current.next
    return lst

# Example usage:
# Creating a linked list from list [1, 2, 3, 4, 5]
head = list_to_linkedlist([1, 2, 3, 4, 5])
solution = Solution()
new_head = solution.removeNthFromEnd(head, 2)

# Converting the updated linked list back to list
print(linkedlist_to_list(new_head))  # Output: [1, 2, 3, 5]
