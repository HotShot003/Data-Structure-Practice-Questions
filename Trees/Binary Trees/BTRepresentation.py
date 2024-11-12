# You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

# Your task to construct a binary tree by creating nodes for the remaining 6 nodes.

# Example:

# Input: 
# nodes = [1 2 3 4 5 6 7]
# Output: 
#          1
#        /   \
#      2       3
#    /  \     /  \
#    4  5    6   7
# Explanation: 
# The 7 node binary tree is represented above.
# Your Task:

# Complete the function void create_tree(node* root0, vector &vec), which takes a root of a Binary tree and vector array vec containing the values of nodes.

# Expected Time Complexity: O(1).

# Expected Auxiliary Space: O(1).

# Constraints:

# vec.length = 7

# 1<=vec[i]<=100

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Solution:
    def createTree(self, root, vec):
        # Ensure that the input list has exactly 7 elements
        if len(vec) != 7:
            return
        
        # Initialize a queue for level-order construction
        queue = [root]
        # print(root.data)
        # print(queue)
        # Start with the second element in the vec list since root is already used
        idx = 1
        
        # Continue until all nodes from the vec list are used
        while idx < len(vec):
            # Get the current node from the queue
            current = queue.pop(0)
            
            # Assign the left child
            current.left = Node(vec[idx])
            queue.append(current.left)
            idx += 1
            
            # Ensure there's still an element for the right child
            if idx < len(vec):
                current.right = Node(vec[idx])
                queue.append(current.right)
                idx += 1
    def printLevelOrder(self, root):
        if root is None:
            return
        
        queue = [root]
        
        while queue:
            # Pop the front element
            current = queue.pop(0)
            
            # Print the current node's data
            print(current.data, end=" ")
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
# Example usage:
nodes = [1, 2, 3, 4, 5, 6, 7]

# Create the root node
root = Node(nodes[0])

# Initialize the solution and create the tree
sol = Solution()
sol.createTree(root, nodes)
sol.printLevelOrder(root)
