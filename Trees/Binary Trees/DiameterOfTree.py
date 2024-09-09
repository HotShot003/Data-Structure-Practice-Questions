# Define a recursive function dia(node, res) that will:
# Compute the height of the left and right subtrees.
# Update the result (maximum diameter so far) with the sum of the left and right subtree heights if it is larger than the current maximum.
# Return the height of the subtree rooted at the current node, which is max(left_height, right_height) + 1.
# Initialize the result as [0], which will store the maximum diameter found.
# Call the recursive function starting from the root node and update the result accordingly.
# Finally, return the maximum diameter stored in res[0].

class Node:
    def __init__(s,data):
        s.data = data
        s.left = None
        s.right = None

class Solution :
    
    def DiameterOfTree(s,root):
        
        def dia(node,res):
            
            if not node:
                return 0 
            
            l = dia(node.left,res)       
            r = dia(node.right,res)       

            res[0] = max(res[0],l+r)
            
            return max(l,r) + 1
        
        res = [0]
        
        dia(root,res)
        
        return res[0]
    

sol = Solution()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(sol.DiameterOfTree(root))