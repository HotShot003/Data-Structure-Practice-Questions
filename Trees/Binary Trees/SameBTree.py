# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

class Node:
    
    def __init__(s,val):
        s.val = val
        s.left = None
        s.right = None

class Tree:
    
    def isSameTree(self,p,q):
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


t = Tree()

root1 = Node(1)    
root1.left = Node(2)    
root1.right = Node(3)

root2 = Node(1)    
root2.left = Node(2)    
root2.right = Node(3)

print(t.isSameTree(root2,root2))    