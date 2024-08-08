# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Step 1: Extract the values from the linked list into a list
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next

        # Step 2: Sort the list
        l.sort()

        # Step 3: Reassign the sorted values back to the linked list nodes
        i = 0
        curr = head
        while curr:
            curr.val = l[i]
            curr = curr.next
            i += 1

        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Example usage
solution = Solution()

# Example 1
head = create_linked_list([4, 2, 1, 3])
sorted_head = solution.sortList(head)
print("Sorted list:", linked_list_to_list(sorted_head))

# Example 2
head = create_linked_list([-1, 5, 3, 4, 0])
sorted_head = solution.sortList(head)
print("Sorted list:", linked_list_to_list(sorted_head))

# Example 3
head = create_linked_list([])
sorted_head = solution.sortList(head)
print("Sorted list:", linked_list_to_list(sorted_head))
