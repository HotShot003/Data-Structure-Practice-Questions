# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Solution :
    
    def levelOrder(self, root):
        if root is None:
            return []
        
        res = []
        q = deque([root])
        
        while q :
            lev = []
            lev_s = len(q)
            
            for _ in range(lev_s):
                node = q.popleft()
                lev.append(node.data)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(lev)
        return res                


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    
    sol = Solution()
    print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]