# Geek loves linked list data structure. Given an array of integer arr of size n, Geek wants to construct the linked list from arr.

# Construct the linked list from arr and return the head of the linked list.

# Example 1:

# Input:
# n = 5
# arr = [1,2,3,4,5]
# Output:
# 1 2 3 4 5
# Explanation: Linked list for the given array will be 1->2->3->4->5.
# Example 2:

# Input:
# n = 2
# arr = [2,4]
# Output:
# 2 4
# Explanation: Linked list for the given array will be 2->4.
# Constraints:
# 1 <= n <= 105
# 1 <= arr[i] <= 100

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function constructLL() which takes arr[] as input parameters and returns the head of the Linked List.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


class Node :
    def __init__(s, data) :
        
        s.data = data 
        s.next = None

class Solution :
    
    def constructLL(s,arr):
        
        if not arr :
            return None
        
        head = Node(arr[0]) 
        curr = head
        
        for val in arr[1:]:
            new_node = Node(val)
            curr.next = new_node
            curr = new_node
    
        return head
    
    def reversell(s,head):
        
        prev = None
        curr = head
        
        while curr :
            
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        return prev    
        
        
    
    
def printLinkedList(head):
        
        curr = head 
        
        while curr :
            print(curr.data,end=" ")
            curr = curr.next
        
        print()





# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    arr1 = [1, 2, 3, 4, 5]
    head1 = sol.constructLL(arr1)
    print("Linked list for arr1:")
    printLinkedList(head1)  # Output: 1 2 3 4 5
    
    reversed_head1 = sol.reversell(head1)
    print("Reversed linked list for arr1:")
    printLinkedList(reversed_head1)  # Output: 5 4 3 2 1
    
    arr2 = [2, 4]
    head2 = sol.constructLL(arr2)
    print("Linked list for arr2:")
    printLinkedList(head2)  # Output: 2 4
    
    reversed_head2 = sol.reversell(head2)
    print("Reversed linked list for arr2:")
    printLinkedList(reversed_head2)  # Output: 4 2