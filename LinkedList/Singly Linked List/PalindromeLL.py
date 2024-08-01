class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        def reverse_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse_list(slow)
        first_half = head

        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

# Example usage:
# Creating a linked list: 1 -> 2 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

solution = Solution()
print(solution.isPalindrome(head))  # Output: True
