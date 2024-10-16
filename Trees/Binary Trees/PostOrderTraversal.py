# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
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
            
            # Ensure there is still a right child to process
            if idx < len(values):
                if values[idx] != -1:
                    current.right = Node(values[idx])
                    queue.append(current.right)
                idx += 1

    def PostorderTraversal(self,node,res):
        
        if not node :
            return 
        
        self.PostorderTraversal(node.left,res)
        self.PostorderTraversal(node.right,res)
        res.append(node.data) 

    def IterPostOrder(self,node):
        
        if not node :
            return []
        
        stk1 = [node]
        stk2 = []
        res = []
        
        while stk1:
            node = stk1.pop()
            stk2.append(node)
            
            if node.left:
                stk1.append(node.left)
            if node.right:
                stk1.append(node.right)
        while stk2:
            node = stk2.pop()
            res.append(node.data)
        return res    
    
    def PostorderTraversal_oneStk(self,node):
        
        if not node:
            return []
        
        stk = [node]
        res = []
        
        while stk:
            node = stk.pop()
            res.append(node.data)
            
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        return res[::-1]
                    
sol = BinaryTree()

sol.insertLevelOrder(values=[1,2,3,4,5,6,7])

Postorder = []

sol.PostorderTraversal(sol.root,Postorder)        
print(Postorder)    
  
                    
print(sol.IterPostOrder(sol.root))

print(sol.PostorderTraversal_oneStk(sol.root))