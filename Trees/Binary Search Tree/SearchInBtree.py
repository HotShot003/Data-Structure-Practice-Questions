# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

class Node:
    def __init__(s,val):
        s.val = val
        s.left = None
        s.right = None
        
def search_bst(root, val):
    """Recursive search in a binary search tree."""
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

# Create a binary search tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

result = search_bst(root, 6)
if result:
    print(f"Found: {result.val}")
else:
    print("Value not found.")
