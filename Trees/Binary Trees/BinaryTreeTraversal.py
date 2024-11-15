# Problem statement
# You have been given a Binary Tree of 'N'

# nodes, where the nodes have integer values.



# Your task is to return the ln-Order, Pre-Order, and Post-Order traversals of the given binary tree.



# For example :
# For the given binary tree:

# The Inorder traversal will be [5, 3, 2, 1, 7, 4, 6].
# The Preorder traversal will be [1, 3, 5, 2, 4, 7, 6].
# The Postorder traversal will be [5, 2, 3, 7, 6, 4, 1].
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 1 2 3 -1 -1 -1  6 -1 -1
# Sample Output 1 :
# 2 1 3 6 
# 1 2 3 6 
# 2 6 3 1
# Explanation of Sample Output 1 :
#  The given binary tree is shown below:

# Inorder traversal of given tree = [2, 1, 3, 6]
# Preorder traversal of given tree = [1, 2, 3, 6]
# Postorder traversal of given tree = [2, 6, 3, 1]
# Sample Input 2 :
# 1 2 4 5 3 -1 -1 -1 -1 -1 -1
# Sample Output 2 :
# 5 2 3 1 4 
# 1 2 5 3 4 
# 5 3 2 4 1
# Explanation of Sample Output 2 :
# The given binary tree is shown below:

# Inorder traversal of given tree = [5, 2, 3, 1, 4]
# Preorder traversal of given tree = [1, 2, 5, 3, 4]
# Postorder traversal of given tree = [5, 3, 2, 4, 1]
# Constraints :
# 1 <= 'N' <= 10^5
# 0 <= 'data' <= 10^5     

# where 'N' is the number of nodes and 'data' denotes the node value of the binary tree nodes.

# Time limit: 1 sec


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
    
    def inorderTraversal(self, node, result):
        if node is None:
            return
        self.inorderTraversal(node.left, result)
        result.append(node.data)
        self.inorderTraversal(node.right, result)
    
    def preorderTraversal(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self.preorderTraversal(node.left, result)
        self.preorderTraversal(node.right, result)
    
    def postorderTraversal(self, node, result):
        if node is None:
            return
        self.postorderTraversal(node.left, result)
        self.postorderTraversal(node.right, result)
        result.append(node.data)

# Sample Input: 1 2 3 -1 -1 -1 6 -1 -1
values = [1, 2, 3, -1, -1, -1, 6]

tree = BinaryTree()
tree.insertLevelOrder(values)

inorder_result = []
preorder_result = []
postorder_result = []

tree.inorderTraversal(tree.root, inorder_result)
tree.preorderTraversal(tree.root, preorder_result)
tree.postorderTraversal(tree.root, postorder_result)

print("In-order Traversal:", inorder_result)
print("Pre-order Traversal:", preorder_result)
print("Post-order Traversal:", postorder_result)
