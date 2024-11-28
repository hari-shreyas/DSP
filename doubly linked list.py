class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def deleteNode(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.insertAtBeginning(10)
    dllist.insertAtEnd(20)
    dllist.insertAtEnd(30)
    dllist.insertAfter(dllist.head, 15)
    dllist.display()
    dllist.deleteNode(dllist.head.next)
    dllist.display()
