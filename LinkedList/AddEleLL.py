# Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

# Examples :

# Input: LinkedList: 1->2->3->4->5 , x = 6
# Output: 1->2->3->4->5->6
# Explanation: 

# We can see that 6 is inserted at the end of the linkedlist.
# Input: LinkedList: 5->4 , x = 1
# Output: 5->4->1
# Explanation: 

# We can see that 1 is inserted at the end of the linkedlist.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 0 <= number of nodes <= 105
# 1 <= node->data , x <= 103


## Add Element At Last :


class Node :
    
    def __init__(s,data):
        s.data = data
        s.next = None


class Solution :
    
    def addElementll(s,head,x):
        
        new_node = Node(x)
        
        if not head :
            return new_node
        
        curr = head 
        
        while curr.next :
            
            curr = curr.next
        
        curr.next = new_node
    
        return head
    

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    print("Original LinkedList 1:")
    printLinkedList(head1)
    head1 = sol.addElementll(head1, 6)
    head1 = sol.addElementll(head1, 7)
    print("Modified LinkedList 1:")
    printLinkedList(head1)
    
    # Example 2
    head2 = Node(5)
    head2.next = Node(4)
    print("Original LinkedList 2:")
    printLinkedList(head2)
    head2 = sol.addElementll(head2, 1)
    print("Modified LinkedList 2:")
    printLinkedList(head2)    
    
        
                    