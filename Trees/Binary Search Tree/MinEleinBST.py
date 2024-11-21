# Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

# Example 1:

# Input:
#            5
#          /    \
#         4      6
#        /        \
#       3          7
#      /
#     1
# Output: 1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def minValue(self, root):
        current = root
        while current and current.left:
            current = current.left
        return current.data if current else None
sol = Solution()
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
root.right.right = Node(7)
root.left.left.left = Node(1)
print("Minimum value in the BST:", sol.minValue(root))
      
        