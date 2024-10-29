# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 

# Follow up: Could you solve it both recursively and iteratively?

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right) if root else True

# Helper function to build a tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    # Example 1
    tree_vals1 = [1, 2, 2, 3, 4, 4, 3]
    root1 = build_tree(tree_vals1)
    print("Tree 1 is symmetric:", is_symmetric(root1))  # Output should be True

    # Example 2
    tree_vals2 = [1, 2, 2, None, 3, None, 3]
    root2 = build_tree(tree_vals2)
    print("Tree 2 is symmetric:", is_symmetric(root2))  # Output should be False
