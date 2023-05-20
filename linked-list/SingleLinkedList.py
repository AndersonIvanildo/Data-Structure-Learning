# Single Linked List Class

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_SingleLinkedList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.nextNode