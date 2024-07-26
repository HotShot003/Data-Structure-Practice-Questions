class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLists(list1, list2):
    # Create a dummy node to serve as the starting point of the merged list
    dummy = Node(0)
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If either list runs out, append the remaining elements of the other list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the head of the merged list
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

# Example usage
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4,5,6,7])
mergedList = mergeTwoLists(list1, list2)
printLinkedList(mergedList)
