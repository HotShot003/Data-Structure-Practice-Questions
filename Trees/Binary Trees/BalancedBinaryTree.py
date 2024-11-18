# Given a binary tree, determine if it is 
# height-balanced

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):

        def check_balance(node):
            # Base case: An empty subtree is balanced and has height 0
            if node is None:
                return 0
            
            # Recursively check the height of the left subtree
            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # If left subtree is not balanced, propagate the result
            
            # Recursively check the height of the right subtree
            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # If right subtree is not balanced, propagate the result
            
            # Check if the current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced
            
            # Return the height of the current subtree
            return max(left_height, right_height) + 1
        
        # Start the recursion from the root
        return check_balance(root) != -1

# Example usage:
if __name__ == "__main__":
    # Example 1: Balanced binary tree
    root1 = Node(3)
    root1.left = Node(9)
    root1.right = Node(20)
    root1.right.left = Node(15)
    root1.right.right = Node(7)

    solution = Solution()
    print(solution.isBalanced(root1))  # Output: True
    
    # Example 2: Unbalanced binary tree
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(2)
    root2.left.left = Node(3)
    root2.left.right = Node(3)
    root2.left.left.left = Node(4)
    root2.left.left.right = Node(4)
    
    print(solution.isBalanced(root2))  # Output: False
    
    # Example 3: Empty tree
    root3 = None
    print(solution.isBalanced(root3))  # Output: True
