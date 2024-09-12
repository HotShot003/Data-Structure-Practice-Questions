# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insertLevelOrder(self, values):
        if not values:
            return None
        
        self.root = Node(values[0])
        queue = [self.root]
        idx = 1
        
        while idx < len(values):
            current = queue.pop(0)
            
            if values[idx] != -1:
                current.left = Node(values[idx])
                queue.append(current.left)
            idx += 1
            
            if idx < len(values):
                if values[idx] != -1:
                    current.right = Node(values[idx])
                    queue.append(current.right)
                idx += 1
    
    def PreorderTraversal_Recur(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self.PreorderTraversal_Recur(node.left, result)
        self.PreorderTraversal_Recur(node.right, result)
    
    def PreorderTraversal_Iter(self, node):
        res = []  
        stk = [node]
        
        while stk:
            node = stk.pop()
            
            if node:
                res.append(node.data)
                stk.append(node.right)  # Push right child first
                stk.append(node.left)   # Push left child after to visit first
        
        return res
sol = BinaryTree()
sol.insertLevelOrder(values=[1, 2, 3, 4, 5, 6, 7])
preorder_Recur = []
sol.PreorderTraversal_Recur(sol.root, preorder_Recur)
preorder_Iter = sol.PreorderTraversal_Iter(sol.root)
print("Recursive Preorder Traversal:", preorder_Recur)
print("Iterative Preorder Traversal:", preorder_Iter)
