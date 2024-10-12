# <!-- Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100 -->

from collections import deque
class Node:
    def __init__(s,val):
        s.val = val
        s.left = None
        s.right = None

class BTree:
    
    def zigzag(s,root):
        
        if root is None:
            return []
        
        res = []
        que = deque([root])
        f = True
        while que:
            lev_s = len(que)
            lev_n = []
            
            for _ in range(lev_s):
                
                node = que.popleft()
                lev_n.append(node.val)
                
                if node.left :
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            if not f:
                lev_n = lev_n[::-1]
            
            res.append(lev_n)
            f = not f
        return res
    
tree = BTree()
root = Node(1)
root.left = Node(2)           
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(tree.zigzag(root))           