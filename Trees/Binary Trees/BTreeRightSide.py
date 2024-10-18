# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        right_view = []
        queue = deque([root])  # Initialize queue with root node
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the rightmost node at the current level, add it to the result
                if i == level_size - 1:
                    right_view.append(node.val)
                
                # Add the children to the queue, right first to ensure rightmost node is processed last
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return right_view

# Example Usage
if __name__ == "__main__":
    # Example 1:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    
    sol = Solution()
    result = sol.rightSideView(root)
    print(result)  # Output: [1, 3, 4]
