# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        s = head
        f = head

        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next

            if f == s:
                s = head

                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None

# Test cases
def test_detectCycle():
    def create_linked_list(values, pos):
        head = None
        tail = None
        cycle_entry = None
        current_pos = 0
        for value in values:
            new_node = Node(value)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            if current_pos == pos:
                cycle_entry = new_node
            
            current_pos += 1
        
        if tail is not None and cycle_entry is not None:
            tail.next = cycle_entry
        
        return head

    solution = Solution()
    
    # Test case 1: No cycle
    head = create_linked_list([1,2,3,4,5,6,3], 2)
    cycle_start = solution.detectCycle(head)
    if cycle_start is None:
        print("Output: no cycle")
    else:
        print(f"Output: tail connects to node index {cycle_start.val}")

    # Test case 2: Cycle exists, starts at index 1
    head = create_linked_list([3, 2, 0, -4], 1)
    cycle_start = solution.detectCycle(head)
    if cycle_start is None:
        print("Output: no cycle")
    else:
        print(f"Output: tail connects to node index {cycle_start.val}")

    # Test case 3: Cycle exists, starts at index 0
    head = create_linked_list([1, 2], 0)
    cycle_start = solution.detectCycle(head)
    if cycle_start is None:
        print("Output: no cycle")
    else:
        print(f"Output: tail connects to node index {cycle_start.val}")

    # Test case 4: Single node with no cycle
    head = create_linked_list([1], -1)
    cycle_start = solution.detectCycle(head)
    if cycle_start is None:
        print("Output: no cycle")
    else:
        print(f"Output: tail connects to node index {cycle_start.val}")

    # Test case 5: Single node with a cycle
    head = create_linked_list([1], 0)
    cycle_start = solution.detectCycle(head)
    if cycle_start is None:
        print("Output: no cycle")
    else:
        print(f"Output: tail connects to node index {cycle_start.val}")

# Run test cases
test_detectCycle()
