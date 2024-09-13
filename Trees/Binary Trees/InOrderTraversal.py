# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
        
        # Create the root of the tree
        self.root = Node(values[0])
        queue = [self.root]
        idx = 1
        
        # Use a queue to construct the tree level by level
        while idx < len(values):
            current = queue.pop(0)
            
            # Add the left child
            if values[idx] != -1:
                current.left = Node(values[idx])
                queue.append(current.left)
            idx += 1
            
            if idx < len(values):
                if values[idx] != -1:
                    current.right = Node(values[idx])
                    queue.append(current.right)
                idx += 1
    
    def InorderTraversal_Recur(self, node, result):
        if node is None:
            return
        self.InorderTraversal_Recur(node.left, result)
        result.append(node.data)
        self.InorderTraversal_Recur(node.right, result)
    
    def InorderTraversal_Iter(self, node):
        res = []
        stk = []
        current = node
        
        while current or stk:
            while current:   
                stk.append(current)
                current = current.left
            
            current = stk.pop()
            res.append(current.data)
            
            current = current.right
            
        return res

sol = BinaryTree()

sol.insertLevelOrder(values=[1, 2, 3, 4, 5, 6, 7])

inorder_Recur = []
sol.InorderTraversal_Recur(sol.root, inorder_Recur)

inorder_Iter = sol.InorderTraversal_Iter(sol.root)

print("Recursive Inorder Traversal:", inorder_Recur)
print("Iterative Inorder Traversal:", inorder_Iter)
