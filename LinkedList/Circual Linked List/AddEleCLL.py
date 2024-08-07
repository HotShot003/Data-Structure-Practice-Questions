class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        elements = []
        if self.head is not None:
            current = self.head
            while True:
                elements.append(current.data)
                current = current.next
                if current == self.head:
                    break
        return elements

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)
# print(cll.head.next.next.next.next.data)
print("Circular Linked List:")
print(cll.display())
