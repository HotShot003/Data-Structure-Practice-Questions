# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100



class Node :
    def __init__(self,data):
        self.data = data
        self.left =  None
        self.right = None

class Solution:
 
    def max_depth(s,root):
        if root is None:
            return 0
        
        l = s.max_depth(root.left)
        r = s.max_depth(root.right)
        
        return max((l,r)) + 1
    

if  __name__ == "__main__" :
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    dep = Solution()
    
    res = dep.max_depth(root)
    print(res)
        