from Node import Node
from SingleLinkedList import SingleLinkedList

sll = SingleLinkedList()
node1 = Node(4)
node2 = Node(1)

sll.head = node1
sll.head.nextNode = node2
sll.tail = node2

sll.print_SingleLinkedList()
